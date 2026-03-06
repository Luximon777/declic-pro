"""
RE'ACTIF PRO API Tests
Tests for pseudonymous authentication and user management
Endpoints tested:
- POST /api/reactif/auth/register - User registration
- POST /api/reactif/auth/login - User login
- GET /api/reactif/user/profile - User profile
- GET /api/reactif/user/results - DE'CLIC PRO results
- POST /api/reactif/user/import-results - Import results via access code
"""

import pytest
import requests
import os
import time

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

class TestReactifProAuth:
    """Test RE'ACTIF PRO authentication endpoints"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test data"""
        self.test_pseudo = f"test_auto_{int(time.time())}"
        self.test_password = "TestPassword123!"
        self.existing_user = {
            "pseudo": "testpro_1772819152",
            "password": "SecurePass123!"
        }
        self.user_with_results = {
            "pseudo": "withcode_1772819271",
            "password": "SecurePass123!"
        }
    
    def test_01_login_existing_user(self):
        """Test login with existing test user"""
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/login",
            json=self.existing_user
        )
        assert response.status_code == 200, f"Login failed: {response.text}"
        
        data = response.json()
        assert data.get("success") == True, "Login should return success=True"
        assert "token" in data, "Login should return a token"
        assert "user" in data, "Login should return user data"
        assert data["user"]["pseudo"] == self.existing_user["pseudo"], "Pseudo should match"
        print(f"Login SUCCESS - User: {data['user']['pseudo']}")
    
    def test_02_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/login",
            json={"pseudo": "nonexistent_user_xyz", "password": "wrongpassword"}
        )
        assert response.status_code == 401, "Invalid login should return 401"
        print("Invalid login correctly rejected")
    
    def test_03_register_new_user(self):
        """Test registration of a new user"""
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/register",
            json={
                "pseudo": self.test_pseudo,
                "password": self.test_password,
                "email_recovery": None,
                "access_code": None,
                "consent_cgu": True,
                "consent_privacy": True,
                "consent_marketing": False
            }
        )
        assert response.status_code == 200, f"Registration failed: {response.text}"
        
        data = response.json()
        assert data.get("success") == True, "Registration should return success=True"
        assert "token" in data, "Registration should return a token"
        assert "user" in data, "Registration should return user data"
        assert data["user"]["pseudo"] == self.test_pseudo, "Pseudo should match"
        print(f"Registration SUCCESS - User: {data['user']['pseudo']}")
    
    def test_04_register_duplicate_pseudo(self):
        """Test registration with duplicate pseudo"""
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/register",
            json={
                "pseudo": self.existing_user["pseudo"],
                "password": "SomePassword123!",
                "consent_cgu": True,
                "consent_privacy": True
            }
        )
        assert response.status_code == 400, "Duplicate registration should return 400"
        print("Duplicate pseudo correctly rejected")
    
    def test_05_register_missing_consents(self):
        """Test registration without required consents"""
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/register",
            json={
                "pseudo": f"test_noconsent_{int(time.time())}",
                "password": "TestPass123!",
                "consent_cgu": False,  # Required consent is false
                "consent_privacy": True
            }
        )
        assert response.status_code == 400, "Registration without CGU consent should fail"
        print("Registration without required consents correctly rejected")


class TestReactifProUserEndpoints:
    """Test RE'ACTIF PRO user data endpoints"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup - login and get token"""
        self.existing_user = {
            "pseudo": "testpro_1772819152",
            "password": "SecurePass123!"
        }
        self.user_with_results = {
            "pseudo": "withcode_1772819271",
            "password": "SecurePass123!"
        }
        
        # Get token for existing user
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/login",
            json=self.existing_user
        )
        if response.status_code == 200:
            self.token = response.json().get("token")
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            self.token = None
            self.headers = {}
    
    def test_06_get_user_profile_authenticated(self):
        """Test get user profile with valid token"""
        if not self.token:
            pytest.skip("No auth token available")
        
        response = requests.get(
            f"{BASE_URL}/api/reactif/user/profile",
            headers=self.headers
        )
        assert response.status_code == 200, f"Profile fetch failed: {response.text}"
        
        data = response.json()
        assert "user" in data, "Response should contain user data"
        assert "profile" in data, "Response should contain profile data"
        print(f"Profile fetch SUCCESS - User: {data['user'].get('pseudo')}")
    
    def test_07_get_user_profile_no_auth(self):
        """Test get user profile without authentication"""
        response = requests.get(
            f"{BASE_URL}/api/reactif/user/profile"
        )
        assert response.status_code == 401, "Unauthenticated profile fetch should return 401"
        print("Unauthenticated profile request correctly rejected")
    
    def test_08_get_user_results_authenticated(self):
        """Test get user results with valid token"""
        if not self.token:
            pytest.skip("No auth token available")
        
        response = requests.get(
            f"{BASE_URL}/api/reactif/user/results",
            headers=self.headers
        )
        assert response.status_code == 200, f"Results fetch failed: {response.text}"
        
        data = response.json()
        assert "results" in data, "Response should contain results array"
        assert isinstance(data["results"], list), "Results should be a list"
        print(f"Results fetch SUCCESS - Found {len(data['results'])} results")
    
    def test_09_get_user_results_with_imported_data(self):
        """Test get user results for user who imported DE'CLIC PRO results"""
        # Login as user with imported results
        login_response = requests.post(
            f"{BASE_URL}/api/reactif/auth/login",
            json=self.user_with_results
        )
        
        if login_response.status_code != 200:
            pytest.skip("User with results not available")
        
        token = login_response.json().get("token")
        headers = {"Authorization": f"Bearer {token}"}
        
        response = requests.get(
            f"{BASE_URL}/api/reactif/user/results",
            headers=headers
        )
        assert response.status_code == 200, f"Results fetch failed: {response.text}"
        
        data = response.json()
        assert "results" in data, "Response should contain results array"
        
        # This user should have imported results
        if len(data["results"]) > 0:
            result = data["results"][0]
            assert "data_type" in result, "Result should have data_type"
            assert "content" in result, "Result should have content"
            print(f"Results with imported data SUCCESS - Found {len(data['results'])} results")
        else:
            print("No imported results found (user may not have imported any)")
    
    def test_10_import_results_invalid_code(self):
        """Test import results with invalid access code"""
        if not self.token:
            pytest.skip("No auth token available")
        
        response = requests.post(
            f"{BASE_URL}/api/reactif/user/import-results",
            headers=self.headers,
            params={"access_code": "INVALID-CODE"}
        )
        assert response.status_code == 404, "Invalid code should return 404"
        print("Invalid access code correctly rejected")


class TestReactifProExportAndDelete:
    """Test RE'ACTIF PRO data export and account deletion"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup - create a test user to potentially delete"""
        self.existing_user = {
            "pseudo": "testpro_1772819152",
            "password": "SecurePass123!"
        }
        
        # Get token
        response = requests.post(
            f"{BASE_URL}/api/reactif/auth/login",
            json=self.existing_user
        )
        if response.status_code == 200:
            self.token = response.json().get("token")
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            self.token = None
            self.headers = {}
    
    def test_11_export_user_data(self):
        """Test GDPR data export endpoint"""
        if not self.token:
            pytest.skip("No auth token available")
        
        response = requests.get(
            f"{BASE_URL}/api/reactif/user/export-data",
            headers=self.headers
        )
        assert response.status_code == 200, f"Data export failed: {response.text}"
        
        data = response.json()
        assert "export_date" in data, "Export should contain date"
        assert "user" in data, "Export should contain user info"
        assert "profile" in data, "Export should contain profile"
        assert "data" in data, "Export should contain user data"
        print(f"Data export SUCCESS - Export date: {data['export_date']}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

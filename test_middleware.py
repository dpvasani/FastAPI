#!/usr/bin/env python3
"""
Test script to verify middleware functionality
"""
import requests
import time
import json

BASE_URL = "http://127.0.0.1:8000"

def test_middleware_demo():
    """Test the middleware demo endpoint"""
    print("🧪 Testing Middleware Demo...")
    
    try:
        response = requests.get(f"{BASE_URL}/middleware-demo/")
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        
        # Check for middleware headers
        print(f"✅ Request ID: {response.headers.get('X-Request-ID', 'Not found')}")
        print(f"✅ Process Time: {response.headers.get('X-Process-Time', 'Not found')}")
        print(f"✅ Response Time: {response.headers.get('X-Response-Time', 'Not found')}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_rate_limiting():
    """Test rate limiting middleware"""
    print("\n🚦 Testing Rate Limiting...")
    
    try:
        # Make multiple requests quickly
        for i in range(5):
            response = requests.get(f"{BASE_URL}/middleware-demo/rate-limit-test")
            print(f"Request {i+1}: Status {response.status_code}")
            time.sleep(0.1)
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_slow_endpoint():
    """Test performance monitoring middleware"""
    print("\n⏱️ Testing Performance Monitoring...")
    
    try:
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/middleware-demo/slow")
        end_time = time.time()
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        print(f"✅ Actual Time: {end_time - start_time:.2f}s")
        print(f"✅ Response Time Header: {response.headers.get('X-Response-Time', 'Not found')}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_error_handling():
    """Test error handling middleware"""
    print("\n🚨 Testing Error Handling...")
    
    try:
        response = requests.get(f"{BASE_URL}/middleware-demo/error")
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_headers():
    """Test request headers middleware"""
    print("\n📋 Testing Request Headers...")
    
    try:
        response = requests.get(f"{BASE_URL}/middleware-demo/headers")
        print(f"✅ Status Code: {response.status_code}")
        data = response.json()
        print(f"✅ Request ID: {data.get('request_id', 'Not found')}")
        print(f"✅ Message: {data.get('message', 'Not found')}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_health_check():
    """Test health check endpoint"""
    print("\n🏥 Testing Health Check...")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all middleware tests"""
    print("🚀 Starting Middleware Tests...\n")
    
    tests = [
        test_middleware_demo,
        test_rate_limiting,
        test_slow_endpoint,
        test_error_handling,
        test_headers,
        test_health_check
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 50)
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All middleware tests passed!")
    else:
        print("⚠️ Some tests failed. Check the output above.")

if __name__ == "__main__":
    main() 
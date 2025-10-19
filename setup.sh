#!/bin/bash
echo "🚀 REMOVING BROKEN PYREBASE..."
pip uninstall -y pyrebase gcloud
echo "✅ INSTALLING PYREBASE4..."
pip install pyrebase4==4.5.0
echo "🎯 INSTALLING OTHER DEPS..."
pip install streamlit python-dotenv

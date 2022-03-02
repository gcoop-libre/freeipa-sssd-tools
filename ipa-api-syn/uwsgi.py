from ipa-api-syn.app import app

"""
Provides UWSGI entrypoint for ipa-api-syn application
"""

if __name__ == "__main__":
    app.run()

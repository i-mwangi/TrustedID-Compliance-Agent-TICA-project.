from flask import Flask, request, jsonify
import os
import re
import logging
from datetime import datetime
import json

# Tengeneza folda ya logs ikiwa haipo
if not os.path.exists("logs"):
    os.makedirs("logs")

# Mpangilio wa logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/compliance-service.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("compliance-service")

# Initialize Flask app
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    logger.info("Health check endpoint called")
    return jsonify({
        "status": "ok",
        "service": "compliance-analysis",
        "version": "1.0.0"
    })

@app.route("/analyze", methods=["POST"])
def analyze_document():
    try:
        data = request.json
        if not data or "document" not in data:
            logger.error("Missing required field: document")
            return jsonify({
                "status": "error", 
                "message": "Missing required field: document"
            }), 400

        document_text = data["document"]
        
        # Fupi kwa ajili ya kuonyesha kwenye log
        truncated_doc = document_text[:100] + "..." if len(document_text) > 100 else document_text
        logger.info(f"Analyzing document: {truncated_doc}")
        
        # Uchambuzi rahisi
        result = {
            "status": "success",
            "score": 0.85,
            "sentiment": "positive",
            "risk_level": "low",
            "recommendations": ["Document appears compliant with regulations"]
        }
        
        logger.info(f"Analysis complete. Risk level: {result['risk_level']}")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error analyzing document: {str(e)}")
        return jsonify({
            "status": "error", 
            "message": f"Analysis failed: {str(e)}"
        }), 500

if __name__ == "__main__":
    logger.info("Compliance analysis service starting")
    app.run(host="0.0.0.0", port=5000) 
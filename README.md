# TrustedID & Compliance Agent (TICA)

A compliance analysis service that combines Hedera blockchain technology with AI capabilities for document verification, identity management, and regulatory compliance.

## Overview

The TrustedID & Compliance Agent (TICA) project provides a robust solution for organizations needing to verify identities, analyze documents for compliance, and maintain an immutable record of transactions. By leveraging the security and transparency of Hedera's distributed ledger technology alongside AI-powered document analysis, TICA offers a comprehensive compliance solution.

## Key Components

### 1. Compliance Analysis Service
- Flask-based API for document analysis
- AI-powered compliance scoring system
- Risk assessment and recommendation engine
- Detailed logging for audit trails

### 2. Hedera Integration
- Identity verification on Hedera's distributed ledger
- Document fingerprinting using Hedera Consensus Service (HCS)
- Token management for access control and incentives
- Secure messaging through Hedera's network

## Features

- **Document Analysis**: AI-powered analysis of documents for compliance with regulations
- **Identity Management**: Secure identity verification using blockchain technology
- **Risk Assessment**: Automated risk scoring for transactions and documents
- **Immutable Record Keeping**: Maintain tamper-proof records of all compliance activities
- **API Integration**: Easy-to-use REST APIs for integration with existing systems

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- Hedera account credentials
- API keys for AI services (if applicable)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/i-mwangi/TrustedID-Compliance-Agent-TICA-project.git
cd TrustedID-Compliance-Agent-TICA-project
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Hedera credentials and other configuration values
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Node.js dependencies (for Hedera integration):
```bash
cd hedera-agent-kit
npm install
```

### Running the Service

1. Start the compliance analysis service:
```bash
python app.py
```

2. The service will be available at `http://localhost:5000`

## API Usage

### Analyze a Document
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"document": "Document text to analyze..."}'
```

### Health Check
```bash
curl -X GET http://localhost:5000/health
```

## Configuration

The system can be configured using environment variables:

- `HEDERA_NETWORK`: Network to connect to (testnet, mainnet)
- `HEDERA_ACCOUNT_ID`: Your Hedera account ID
- `HEDERA_PRIVATE_KEY`: Your Hedera private key
- `PORT`: Port for the API server
- `COMPLIANCE_SERVICE_URL`: URL for the compliance service
- `RISK_SERVICE_URL`: URL for the risk assessment service

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Project Link: [https://github.com/i-mwangi/TrustedID-Compliance-Agent-TICA-project](https://github.com/i-mwangi/TrustedID-Compliance-Agent-TICA-project) 
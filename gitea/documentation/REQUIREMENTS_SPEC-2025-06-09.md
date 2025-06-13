# Requirements Specification: Gitea Git Server for Isengard

## 1. Project Overview

### 1.1 Purpose

This project aims to deploy a lightweight, easy-to-maintain git server (Gitea) in an Isengard account to facilitate teaching coding on AWS. The git server will primarily host demo projects and educational repositories, requiring minimal administrative overhead while providing essential git functionality.

### 1.2 Scope

The scope includes the deployment, configuration, and maintenance of a Gitea git server, including backup mechanisms and secure access. The implementation should prioritize simplicity and ease of maintenance over advanced features.

### 1.3 Definitions

- **Gitea**: A lightweight, self-hosted git service written in Go, forked from Gogs
- **Isengard**: AWS internal account management service
- **Git**: Distributed version control system
- **EBS**: Amazon Elastic Block Store
- **S3**: Amazon Simple Storage Service

## 2. Functional Requirements

### 2.1 Core Git Functionality

- FR1.1: The system shall provide standard git operations (clone, push, pull, merge).
- FR1.2: The system shall support creating, viewing, and managing git repositories through a web interface.
- FR1.3: The system shall support basic code review functionality including pull requests and code comments.
- FR1.4: The system shall display commit history, branches, and tags for each repository.

### 2.2 User Management
- FR2.1: The system shall support local user account creation and management within Gitea.
- FR2.2: The system shall support basic permission levels (read, write, admin) for repositories.
- FR2.3: The system shall accommodate 1-5 user accounts.
- FR2.4: The system shall support up to 50 repositories (with expected usage around 10 repositories).

### 2.3 Repository Management

- FR3.1: The system shall allow creation of public and private repositories.
- FR3.2: The system shall store repository data on persistent EBS storage.
- FR3.3: The system shall provide basic repository statistics and insights.
- FR3.4: The system shall allow repository owners to manage repository settings and access.

### 2.4 Backup and Recovery

- FR4.1: The system shall perform automated backups of repositories to Amazon S3.
- FR4.2: The system shall maintain a backup history to allow for repository restoration if needed.
- FR4.3: The system shall provide a mechanism to restore repositories from backups.

## 3. Non-Functional Requirements

### 3.1 Performance

- NFR1.1: The system shall support concurrent access by up to 5 users.
- NFR1.2: The system shall handle repositories primarily containing text files efficiently.
- NFR1.3: The system shall optimize for read operations over write operations.

### 3.2 Security

- NFR2.1: All access to the git server shall be secured with HTTPS.
- NFR2.2: The system shall enforce user authentication for repository access.
- NFR2.3: The system shall implement secure credential storage.

### 3.3 Availability

- NFR3.1: The system shall be available during teaching demonstrations.
- NFR3.2: The system can have occasional maintenance windows as needed.
- NFR3.3: The system shall maintain data integrity across restarts.

### 3.4 Usability

- NFR4.1: The system shall provide an intuitive web interface for repository management.
- NFR4.2: The system shall be accessible via standard git clients.
- NFR4.3: The system shall provide clear error messages for failed operations.

### 3.5 Maintainability

- NFR5.1: The system shall be deployed using Docker containers for ease of management.
- NFR5.2: The system shall support straightforward version updates.
- NFR5.3: The system shall log key operations for troubleshooting.

## 4. Technical Constraints

### 4.1 Deployment Environment

- TC1.1: The system shall be deployed in an Isengard AWS account.
- TC1.2: The system shall be deployed in the us-west-2 region.
- TC1.3: The system shall use EC2 for compute resources.

### 4.2 Storage

- TC2.1: Repository data shall be stored on EBS volumes for persistence.
- TC2.2: Backups shall be stored in Amazon S3.
- TC2.3: The system shall be optimized for storing and versioning text files.

### 4.3 Networking

- TC3.1: The system shall be accessible over the public internet.
- TC3.2: The system shall use an AWS-provided URL for access.
- TC3.3: All network traffic shall be encrypted via HTTPS.

## 5. User Personas

### 5.1 Instructor

**Name**: Alex
**Role**: Technical instructor who teaches AWS coding concepts
**Goals**:

- Host demo code repositories for teaching purposes
- Provide students with example code
- Create branches to demonstrate different concepts
- Track changes in code over time during demonstrations

### 5.2 Student

**Name**: Jamie
**Role**: Student learning AWS development
**Goals**:

- Access example code repositories
- Clone repositories to follow along with demonstrations
- Submit code changes via pull requests
- Track personal progress through commit history

## 6. Success Criteria

### 6.1 Implementation Success

- SC1.1: Gitea git server successfully deployed and accessible via the public internet
- SC1.2: Authentication system configured and functional
- SC1.3: Repository creation and management working as expected
- SC1.4: Automated backup system configured and operational

### 6.2 Operational Success

- SC2.1: System remains available and functional during teaching demonstrations
- SC2.2: System requires minimal maintenance intervention
- SC2.3: Repository data remains intact and accessible over time
- SC2.4: System can be efficiently updated when needed

## 7. Future Considerations (v2.0)

### 7.1 Binary File Support

- FC1.1: Improved handling of binary files
- FC1.2: Efficient storage and versioning of binary assets

### 7.2 Advanced Features

- FC2.1: Integration with CI/CD pipelines
- FC2.2: Enhanced code review features
- FC2.3: Additional authentication options
# 🤝 Contributing to HF Vision Demo

Thank you for your interest in contributing to the HF Vision Demo project! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Community](#community)

## 📜 Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Unacceptable Behavior

Examples of unacceptable behavior include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## 🚀 Getting Started

### Prerequisites

Before contributing, make sure you have:

- Python 3.9+ installed
- Git for version control
- A GitHub account
- Basic knowledge of FastAPI and JavaScript
- Familiarity with computer vision concepts (helpful but not required)

### First Steps

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/huggin-face.git
   cd huggin-face/hf-vision-demo
   ```
3. **Set up the development environment** (see [DEVELOPMENT.md](hf-vision-demo/DEVELOPMENT.md))
4. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ How to Contribute

### Types of Contributions

We welcome various types of contributions:

#### 🐛 Bug Reports
- Use the bug report template
- Include steps to reproduce
- Provide system information
- Add screenshots if applicable

#### ✨ Feature Requests
- Use the feature request template
- Explain the use case
- Describe the proposed solution
- Consider implementation complexity

#### 📝 Documentation
- Fix typos and grammar
- Improve clarity and examples
- Add missing documentation
- Translate to other languages

#### 💻 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Test coverage improvements

#### 🎨 UI/UX Improvements
- Frontend enhancements
- Better user experience
- Accessibility improvements
- Mobile responsiveness

## 🔧 Development Setup

Detailed setup instructions are available in [DEVELOPMENT.md](hf-vision-demo/DEVELOPMENT.md). Quick setup:

```bash
# Clone and setup
git clone https://github.com/YOUR_USERNAME/huggin-face.git
cd huggin-face/hf-vision-demo

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start development server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## 📏 Coding Standards

### Python Code Style

We follow PEP 8 with some modifications:

```bash
# Format code with Black
black backend/ *.py

# Lint with flake8
flake8 backend/ *.py --max-line-length=88

# Type checking with mypy
mypy backend/main.py
```

#### Code Style Guidelines

- **Line length**: Maximum 88 characters
- **Imports**: Use absolute imports, group by standard/third-party/local
- **Docstrings**: Use Google-style docstrings
- **Type hints**: Add type hints for function parameters and returns
- **Variable names**: Use descriptive names, snake_case for variables and functions

#### Example Code Style

```python
from typing import List, Dict, Any
from fastapi import FastAPI, UploadFile, File
from PIL import Image


def process_image(image: Image.Image, model_name: str) -> Dict[str, Any]:
    """Process an image using the specified model.
    
    Args:
        image: PIL Image object to process
        model_name: Name of the model to use for processing
        
    Returns:
        Dictionary containing processing results
        
    Raises:
        ValueError: If model_name is not supported
    """
    if model_name not in SUPPORTED_MODELS:
        raise ValueError(f"Unsupported model: {model_name}")
    
    # Process image...
    return {"model": model_name, "results": results}
```

### JavaScript Code Style

- **ES6+**: Use modern JavaScript features
- **Const/Let**: Prefer `const` and `let` over `var`
- **Arrow functions**: Use arrow functions for short functions
- **Async/Await**: Prefer async/await over promises
- **Comments**: Add comments for complex logic

#### Example JavaScript Style

```javascript
// Good
const captureImage = async () => {
  try {
    const blob = await captureBlob();
    return blob;
  } catch (error) {
    console.error('Failed to capture image:', error);
    throw error;
  }
};

// Avoid
function captureImage() {
  return captureBlob().then(function(blob) {
    return blob;
  }).catch(function(error) {
    console.log(error);
  });
}
```

### HTML/CSS Style

- **Semantic HTML**: Use appropriate HTML5 elements
- **CSS Classes**: Use descriptive class names
- **Responsive Design**: Ensure mobile compatibility
- **Accessibility**: Add proper ARIA labels and alt text

## 🔄 Pull Request Process

### Before Submitting

1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Add tests** for new functionality
4. **Ensure code style** compliance
5. **Update CHANGELOG** if applicable

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tested locally
- [ ] Added unit tests
- [ ] Updated integration tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Review Process

1. **Automated checks** must pass (linting, tests)
2. **Code review** by maintainers
3. **Testing** on different environments
4. **Approval** and merge

## 📝 Issue Guidelines

### Bug Reports

Use this template for bug reports:

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Go to...
2. Click on...
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.10.0]
- Browser: [e.g., Chrome 95.0]

**Additional Context**
Screenshots, logs, etc.
```

### Feature Requests

Use this template for feature requests:

```markdown
**Feature Description**
Clear description of the feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this be implemented?

**Alternatives Considered**
Other solutions you've considered

**Additional Context**
Mockups, examples, etc.
```

## 🏷️ Labels and Milestones

### Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements or additions to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed
- `question`: Further information is requested
- `wontfix`: This will not be worked on

### Priority Labels

- `priority: high`: Critical issues
- `priority: medium`: Important issues
- `priority: low`: Nice to have

## 🌟 Recognition

Contributors will be recognized in:

- **README.md**: Contributors section
- **CHANGELOG.md**: Release notes
- **GitHub**: Contributor graphs and statistics

## 💬 Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and collaboration

### Getting Help

1. **Check documentation**: README, DEVELOPMENT.md, API.md
2. **Search existing issues**: Someone might have asked already
3. **Create a new issue**: Use appropriate templates
4. **Join discussions**: Share ideas and get feedback

### Mentorship

New contributors can:

- **Start with good first issues**: Look for `good first issue` label
- **Ask questions**: Don't hesitate to ask for help
- **Pair programming**: Request code review and feedback
- **Documentation**: Start with documentation improvements

## 📚 Resources

### Learning Materials

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Python Style Guide](https://pep8.org/)

### Tools

- [VS Code](https://code.visualstudio.com/): Recommended IDE
- [GitHub Desktop](https://desktop.github.com/): Git GUI
- [Postman](https://www.postman.com/): API testing

## 🙏 Thank You

Thank you for contributing to HF Vision Demo! Your contributions help make this project better for everyone.

---

**Questions?** Feel free to open an issue or start a discussion. We're here to help! 🚀

from fastapi import APIRouter  
from app.models.project import Project

"""
Mocking the real data to be displayed in our project 
"""

router = APIRouter()
projects = [
    Project(
        id=1,
        title="Wildlife Conservation – Image Classification System",
        description=(
            "A deep learning system that classifies wildlife species from images "
            "using convolutional neural networks. The project includes a full "
            "training pipeline with preprocessing, augmentation, GPU acceleration, "
            "and reproducibility controls."
        ),
        technologies=[
            "Python",
            "PyTorch",
            "CNNs",
            "NumPy",
            "Machine Learning",
            "Computer Vision"
        ],
        github_url="https://github.com/yourusername/wildlife-image-classification"
    ),
    Project(
        id=2,
        title="S-M Software Solutions Platform",
        description=(
            "A full-stack enterprise platform developed with .NET Core and MVC "
            "architecture. Focused on secure role-based authentication, reusable "
            "service layers, and scalable backend design."
        ),
        technologies=[
            ".NET Core",
            "C#",
            "ASP.NET MVC",
            "ASP.NET Identity",
            "Razor Pages",
            "SQL"
        ],
        github_url="https://github.com/yourusername/sm-software-platform"
    ),
    Project(
        id=3,
        title="Spring Boot Soccer League Platform",
        description=(
            "A soccer league management web application built using Java Spring Boot "
            "and React. Implements JWT authentication, MongoDB persistence, "
            "RabbitMQ messaging, and RESTful APIs."
        ),
        technologies=[
            "Java",
            "Spring Boot",
            "React",
            "MongoDB",
            "JWT",
            "RabbitMQ",
            "REST APIs"
        ],
        github_url="https://github.com/yourusername/soccer-league-platform"
    )
]
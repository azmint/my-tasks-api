# Source

## Base Design
Domain Driven Design

## Layer

### Dependencies
infrastructure -> interface -> command.usecase -> command.domain

### command.domain
* Value Object
* Entity
* Repository Interface
* Event

### command.usecase
* Service
* Coordinator

### infrastructure
* Repository Implements
* External Library
* Rooting

### interface
* Controller
* Validator

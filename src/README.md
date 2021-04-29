# Source

## Base Design
Domain Driven Design

## Layer
* Externally-independent library
  * injector
  * cerberus

### Dependencies
infrastructure -> interface -> usecase -> domain

### domain
* Value Object
* Entity
* Repository Interface
* Event

### usecase
* Service
* Coordinator

### infrastructure
* Repository Implements
* Externally dependent libraries
* Rooting

### interface
* Controller
* Validator

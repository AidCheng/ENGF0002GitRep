
# Target for spec

- non-python specific
- indicates how receved values be sanity-checked (whether the number is legal)
- clean / either text-based or binary coded (consistent)
- less chatty (appropriate messages for each update)
- Can use TCP / UDP or both

# Task

- The protocol must not use `pickle`
- The protocol must not use `HTML. XML, JSON`
- Specify how to encode the information currently sent in all 12 existing messages
- Specify any additional processing the receiver should perform on recept of the message (*not already performed in the existing code*)


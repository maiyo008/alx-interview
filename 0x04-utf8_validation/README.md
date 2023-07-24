# 0x04-utf8_validation
---
## UTF-8 Explained
UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding scheme that is widely used to represent text in computers and communication systems. It is part of the larger Unicode standard, which aims to provide a unique numeric code point for every character in all the world's writing systems, including characters from various languages, symbols, and special characters.

In UTF-8, each character is represented by a variable number of 8-bit bytes. The basic idea is that ASCII characters (which use 7 bits) are represented using a single byte (0 to 127), while other characters outside the ASCII range are represented using multiple bytes. The number of bytes used to represent a character depends on its Unicode code point value.

![UTF-8 encoding](https://i.imgur.com/vIuC0b6.png)

## Resources
**Read or watch:**

* [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
* [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
---
## Tasks 0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: def validUTF8(data)
* Return: True if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
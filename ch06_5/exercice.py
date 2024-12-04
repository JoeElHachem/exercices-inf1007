#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	opening_brackets = brackets[::2]
	closing_brackets = brackets[1::2]
	bracket_map = dict(zip(closing_brackets, opening_brackets))
	stack = []

	for char in text:
		if char in opening_brackets:
			stack.append(char)
		elif char in closing_brackets:
			if not stack or stack[-1] != bracket_map[char]:
				return False
			stack.pop()

	return not stack

def remove_comments(full_text, comment_start, comment_end):
	while True:
		start = full_text.find(comment_start)
		end = full_text.find(comment_end)
		if start == -1 and end == -1:
			return full_text
		if end < start or (start == -1) != (end == -1):
			return None
		full_text = full_text[:start] + full_text[end + len(comment_end):]


def get_tag_prefix(text, opening_tags, closing_tags):
	for otag, ctag in zip(opening_tags, closing_tags):
		if text.startswith(otag):
			return (otag, None)
		elif text.startswith(ctag):
			return (None, ctag)



def check_tags(full_text, tag_names, comment_tags):
	text = remove_comments(full_text, *comment_tags)
	if text is None:
		return False
	opening_tags = {f"<{name}>": f"</{name}>" for name in tag_names}
	closing_tags = dict((v, k) for k, v in opening_tags.items())

	tag_stack = []
	while len(text) != 0:
		opening, closing = get_tag_prefix(text, opening_tags.keys(), closing_tags.keys())

		if opening is not None:

			tag_stack.append(opening)
			text = text[len(opening):]

		elif closing is not None:

			if len(tag_stack) == 0 or tag_stack[-1] != closing_tags[closing]:

				return False

			tag_stack.pop()
			text = text[len(closing):]

		else:

			text = text[1:]

	return len(tag_stack) == 0



if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()


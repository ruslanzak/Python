#!/usr/bin/env python3

print("Content-type: text/html")
print()
q = 10
i = 0
print("<table border='1px' style='border-collapse:collapse;'>")
print("<tr>")
while i <= q:
	print("<td style='font-weight:600;'>")
	if i != 0:
		print(i)
	print("</td>")
	i += 1
print("</tr>")

i = 1
while i <= q:
	print("<tr>")
	j = 0
	while j <= q:
		style = ""
		if j == 0:
			print("<td style='font-weight:600;'>", i, "</td>")
		else:
			print("<td", style, ">", i * j, "</td>")
		j += 1
	print("</tr>")
	i += 1
print("</table>")
	

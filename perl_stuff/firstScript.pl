#!/usr/bin/perl -w

## use strict;
## use warnings;

my $secretword = "truc";

print ("What's your name?\n");
$name = <STDIN>;
chomp ($name);

if ($name eq "patate")
{
	print("Hello to you, $name! My vegetable friend !\n");
}
else
{
	print("Hello, $name\n");
	print("what is the secret word ? ");
	$guess = <STDIN>;
	chomp($guess);
	while ($guess ne $secretword)
	{
		print("$guess is wrong, try gain. What is the secret word? ");
		$guess = <STDIN>;
		chomp($guess);
		
	}
}


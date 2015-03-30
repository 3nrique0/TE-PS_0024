#!/usr/bin/perl -w

## use strict;
use warnings;

%words = qw(
	fred	camel
	barney	llama
	betty	alpaca
	wilma	alpaca
);

print ("What's your name?\n");
$name = <STDIN>;
chomp ($name);

if ($name =~ /^randal\b/i) {
	print("Hello to you, $name! Good of you to be here !\n");
}

else {
	$secretword = $words{$name};
	print("Hello, $name\n");
	if ($secretword eq "") {
		$secretword = "groucho";
	}
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


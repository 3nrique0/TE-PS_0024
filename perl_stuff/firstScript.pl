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
# $original_name = $name;

# $name =~ s/\W.*//;
# $name =~ tr/A-Z/a-z/;


if ($name =~ /^randal\b/i) {
	print("Hello to you, $name! Good of you to be here !\n");
}

else {
# 	$secretword = $words{$name};
	print("Hello, $name\n");

# 	if ($secretword eq "") {
# 		$secretword = "groucho";
# 	}

	print("what is the secret word ? ");
	$guess = <STDIN>;
	chomp($guess);

# 	while ($guess ne $secretword)
# 	{
# 		print("$guess is wrong, try gain. What is the secret word? ");
# 		$guess = <STDIN>;
# 		chomp($guess);
# 		
# 	}

	while (! good_word($name,$guess)){
		print "Wrongm try agaun. What is the secret word? ";
		$guess = <STDIN>;
		chomp($guess) 
	}
}




sub good_word {
	my($somename, $someguess) = @_;		# nomer les paramètres
	$somename =~ s/\W.*//;			# se debarrasser de tout ce qui suit le premier mot
	$somename =~ ~ tr/A-Z/a-z/;		# tout en minuscules
	
	if ($somename eq "randal") {
		return 1;			# valeur de retour == true
	} elsif (($words{$somename} || "groucho") eq $someguess) {
		return 1;			# valeur de retour == true
	} else {
	return 0; 				# valeur de retour == false
	}
}



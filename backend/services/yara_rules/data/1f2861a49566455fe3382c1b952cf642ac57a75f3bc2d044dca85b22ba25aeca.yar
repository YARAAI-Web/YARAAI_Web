rule auto_rule_20250727042806_6799 {
  strings:
    $o0 = "off_401BC0" wide ascii nocase
  condition:
    all of them
}
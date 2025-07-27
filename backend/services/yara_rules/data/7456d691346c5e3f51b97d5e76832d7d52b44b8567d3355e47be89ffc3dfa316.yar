rule auto_rule_20250726191403_9773 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "x406891" wide ascii nocase
    $o2 = "x_ismbbtype" wide ascii nocase
  condition:
    3 of ($o*)
}
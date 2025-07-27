rule auto_rule_20250727022349_9225 {
  strings:
    $o0 = "byte_4698BE" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "mbtowc" wide ascii nocase
  condition:
    3 of ($o*)
}
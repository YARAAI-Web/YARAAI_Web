rule auto_rule_20250726102840_3292 {
  strings:
    $o0 = "x_ismbbtype" wide ascii nocase
    $o1 = "off_46750C" wide ascii nocase
  condition:
    all of them
}
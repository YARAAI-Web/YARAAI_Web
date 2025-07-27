rule auto_rule_20250726131457_1499 {
  strings:
    $o0 = "x6D5600004239LL" wide ascii nocase
    $o1 = "x4EED" wide ascii nocase
    $o2 = "x58B2u" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726073904_2091 {
  strings:
    $o0 = "StringType" wide ascii nocase
    $o1 = "x54D200007DF1LL" wide ascii nocase
    $o2 = "x98678765" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726114016_0689 {
  strings:
    $o0 = "asserts" wide ascii nocase
    $o1 = "strcat" wide ascii nocase
    $o2 = "bKeyDown" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
    $o4 = "off_467750" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726082716_3945 {
  strings:
    $o0 = "word_1E696" wide ascii nocase
    $o1 = "systemroot" wide ascii nocase
    $o2 = "x61737973u" wide ascii nocase
    $o3 = "dword_78318" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}
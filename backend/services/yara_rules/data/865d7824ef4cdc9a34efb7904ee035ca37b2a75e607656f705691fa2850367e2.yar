rule auto_rule_20250726141144_8369 {
  strings:
    $o0 = "dword_457E04" wide ascii nocase
    $o1 = "x1004u" wide ascii nocase
    $o2 = "_fpmath" wide ascii nocase
    $o3 = "dword_45777C" wide ascii nocase
    $o4 = "TrailDown1" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250727015710_5198 {
  strings:
    $o0 = "dword_40BB48" wide ascii nocase
    $o1 = "byte_401BD0" wide ascii nocase
    $o2 = "dword_40C590" wide ascii nocase
  condition:
    3 of ($o*)
}
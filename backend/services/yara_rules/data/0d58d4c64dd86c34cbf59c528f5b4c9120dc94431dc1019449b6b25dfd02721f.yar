rule auto_rule_20250726221857_2159 {
  strings:
    $o0 = "_except_handler3" wide ascii nocase
    $o1 = "byte_450181" wide ascii nocase
    $o2 = "dword_44FFD4" wide ascii nocase
    $o3 = "x415710" wide ascii nocase
  condition:
    4 of ($o*)
}
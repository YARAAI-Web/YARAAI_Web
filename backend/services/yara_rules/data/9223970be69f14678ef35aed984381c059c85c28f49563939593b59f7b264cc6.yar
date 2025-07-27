rule auto_rule_20250727034407_3411 {
  strings:
    $o0 = "dword_408018" wide ascii nocase
    $o1 = "__ld12mul" wide ascii nocase
    $o2 = "dword_40BCEC" wide ascii nocase
    $o3 = "_abstract_cw" wide ascii nocase
    $o4 = "dword_40BCC4" wide ascii nocase
  condition:
    4 of ($o*)
}
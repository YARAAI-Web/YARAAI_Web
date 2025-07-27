rule auto_rule_20250727030615_1727 {
  strings:
    $o0 = "__sbh_verify_block" wide ascii nocase
    $o1 = "_ioinit" wide ascii nocase
    $o2 = "dword_4693F0" wide ascii nocase
    $o3 = "byte_4673C6" wide ascii nocase
  condition:
    4 of ($o*)
}
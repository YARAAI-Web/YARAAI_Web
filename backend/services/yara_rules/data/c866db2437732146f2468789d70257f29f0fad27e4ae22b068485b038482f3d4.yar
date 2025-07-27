rule auto_rule_20250727021252_9732 {
  strings:
    $o0 = "byte_4C10C2" wide ascii nocase
    $o1 = "x5Bu" wide ascii nocase
    $o2 = "dword_4C131C" wide ascii nocase
    $o3 = "xF4u" wide ascii nocase
    $o4 = "dword_4C170C" wide ascii nocase
  condition:
    4 of ($o*)
}
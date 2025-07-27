rule auto_rule_20250727030010_7112 {
  strings:
    $o0 = "ReturnSize" wide ascii nocase
    $o1 = "dword_6EB43108" wide ascii nocase
    $o2 = "dword_6EB4305C" wide ascii nocase
  condition:
    3 of ($o*)
}
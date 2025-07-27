rule auto_rule_20250726131904_1674 {
  strings:
    $o0 = "dword_12F0558" wide ascii nocase
    $o1 = "dword_12F074C" wide ascii nocase
    $o2 = "dword_12F041C" wide ascii nocase
    $o3 = "dword_12F0528" wide ascii nocase
  condition:
    4 of ($o*)
}
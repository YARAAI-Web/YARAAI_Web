rule auto_rule_20250726234653_0194 {
  strings:
    $o0 = "byte_4602B8" wide ascii nocase
    $o1 = "dword_460140" wide ascii nocase
    $o2 = "dword_460734" wide ascii nocase
    $o3 = "dword_4605D4" wide ascii nocase
    $o4 = "byte_460780" wide ascii nocase
  condition:
    4 of ($o*)
}
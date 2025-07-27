rule auto_rule_20250727011212_3610 {
  strings:
    $o0 = "dword_4642CC" wide ascii nocase
    $o1 = "VisualC" wide ascii nocase
    $o2 = "byte_460EB0" wide ascii nocase
    $o3 = "xC000008E" wide ascii nocase
  condition:
    4 of ($o*)
}
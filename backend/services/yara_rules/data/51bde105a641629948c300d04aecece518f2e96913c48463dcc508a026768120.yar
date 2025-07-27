rule auto_rule_20250726215207_1111 {
  strings:
    $o0 = "dword_4C1714" wide ascii nocase
    $o1 = "dword_4C128C" wide ascii nocase
    $o2 = "byte_4C10C2" wide ascii nocase
    $o3 = "ExpandEnvStrings" wide ascii nocase
  condition:
    4 of ($o*)
}
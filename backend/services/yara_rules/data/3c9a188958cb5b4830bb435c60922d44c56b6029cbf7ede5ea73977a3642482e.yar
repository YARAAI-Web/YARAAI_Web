rule auto_rule_20250726140618_4455 {
  strings:
    $o0 = "dword_44BE78" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "dodwords" wide ascii nocase
    $o3 = "dword_44BEA4" wide ascii nocase
  condition:
    4 of ($o*)
}
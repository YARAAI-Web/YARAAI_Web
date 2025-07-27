rule auto_rule_20250726061016_7573 {
  strings:
    $o0 = "dword_475D20" wide ascii nocase
    $o1 = "x1004u" wide ascii nocase
    $o2 = "off_418130" wide ascii nocase
    $o3 = "dword_47568C" wide ascii nocase
  condition:
    4 of ($o*)
}
rule auto_rule_20250726185738_8613 {
  strings:
    $o0 = "dword_45D500" wide ascii nocase
    $o1 = "strncnt" wide ascii nocase
    $o2 = "dword_45D3CC" wide ascii nocase
    $o3 = "dword_450018" wide ascii nocase
    $o4 = "dword_45CFC8" wide ascii nocase
  condition:
    4 of ($o*)
}
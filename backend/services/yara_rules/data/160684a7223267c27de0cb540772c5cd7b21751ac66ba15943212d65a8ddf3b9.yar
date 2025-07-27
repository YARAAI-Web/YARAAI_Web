rule auto_rule_20250726135230_3385 {
  strings:
    $o0 = "strncnt" wide ascii nocase
    $o1 = "dword_45D508" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
    $o3 = "__crtMessageBoxA" wide ascii nocase
    $o4 = "xcptlookup" wide ascii nocase
  condition:
    5 of ($o*)
}
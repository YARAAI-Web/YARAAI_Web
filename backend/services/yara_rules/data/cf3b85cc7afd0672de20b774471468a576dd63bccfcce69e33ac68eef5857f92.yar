rule auto_rule_20250727040337_1763 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "dword_45FD40" wide ascii nocase
    $o2 = "strncnt" wide ascii nocase
    $o3 = "dword_445018" wide ascii nocase
  condition:
    4 of ($o*)
}
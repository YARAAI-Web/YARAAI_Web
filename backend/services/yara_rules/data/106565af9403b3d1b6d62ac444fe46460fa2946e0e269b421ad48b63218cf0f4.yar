rule auto_rule_20250726141801_5152 {
  strings:
    $o0 = "dword_45CB04" wide ascii nocase
    $o1 = "dword_45C2DC" wide ascii nocase
    $o2 = "nProgram" wide ascii nocase
    $o3 = "dword_45CEF4" wide ascii nocase
    $o4 = "byte_45CC14" wide ascii nocase
  condition:
    4 of ($o*)
}
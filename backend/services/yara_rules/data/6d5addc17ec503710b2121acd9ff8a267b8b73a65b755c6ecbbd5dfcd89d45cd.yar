rule auto_rule_20250726163951_0751 {
  strings:
    $o0 = "dword_100064F4" wide ascii nocase
    $o1 = "aligned_malloc" wide ascii nocase
    $o2 = "CreateDIBSection" wide ascii nocase
    $o3 = "dword_100061CC" wide ascii nocase
    $o4 = "qword_10006510" wide ascii nocase
  condition:
    4 of ($o*)
}
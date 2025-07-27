rule auto_rule_20250726085118_3945 {
  strings:
    $o0 = "dword_42F628" wide ascii nocase
    $o1 = "dword_42F600" wide ascii nocase
    $o2 = "GetClassInfoExAGetClassInfoExAGetClassInfoExAGetClassInfoExA" wide ascii nocase
    $o3 = "dword_42F5F4" wide ascii nocase
    $o4 = "dword_42F570" wide ascii nocase
  condition:
    4 of ($o*)
}
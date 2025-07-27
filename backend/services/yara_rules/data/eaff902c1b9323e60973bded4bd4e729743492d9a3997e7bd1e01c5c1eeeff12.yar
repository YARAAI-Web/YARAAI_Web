rule auto_rule_20250726203109_6874 {
  strings:
    $o0 = "_IsZeroMan" wide ascii nocase
    $o1 = "dword_42089C" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "StringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}
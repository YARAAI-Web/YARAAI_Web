rule auto_rule_20250726202425_3504 {
  strings:
    $o0 = "_updatetlocinfoEx_nolock" wide ascii nocase
    $o1 = "dword_401130" wide ascii nocase
    $o2 = "dword_40C43C" wide ascii nocase
    $o3 = "dword_401418" wide ascii nocase
  condition:
    4 of ($o*)
}
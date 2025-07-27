rule auto_rule_20250726191939_4821 {
  strings:
    $o0 = "dword_42FD72" wide ascii nocase
    $o1 = "FatDate" wide ascii nocase
    $o2 = "x5EA20000693ELL" wide ascii nocase
    $o3 = "off_41B27C" wide ascii nocase
    $o4 = "pszPort" wide ascii nocase
  condition:
    4 of ($o*)
}
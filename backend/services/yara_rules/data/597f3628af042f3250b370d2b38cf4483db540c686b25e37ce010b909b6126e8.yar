rule auto_rule_20250727025348_3867 {
  strings:
    $o0 = "dword_4336B3" wide ascii nocase
    $o1 = "pszFaceName" wide ascii nocase
    $o2 = "dword_4336E7" wide ascii nocase
    $o3 = "hrgnSrc2" wide ascii nocase
  condition:
    4 of ($o*)
}
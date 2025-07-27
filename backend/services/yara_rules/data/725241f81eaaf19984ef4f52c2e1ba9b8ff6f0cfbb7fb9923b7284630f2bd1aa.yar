rule auto_rule_20250726110309_8498 {
  strings:
    $o0 = "x1C7B" wide ascii nocase
    $o1 = "dword_42E7CC" wide ascii nocase
    $o2 = "dword_4304D3" wide ascii nocase
    $o3 = "x39EDu" wide ascii nocase
    $o4 = "pszFaceName" wide ascii nocase
  condition:
    4 of ($o*)
}
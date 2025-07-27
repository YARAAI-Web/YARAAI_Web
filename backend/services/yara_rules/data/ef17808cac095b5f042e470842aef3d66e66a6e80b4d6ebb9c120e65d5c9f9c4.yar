rule auto_rule_20250726131542_0085 {
  strings:
    $o0 = "dword_44E834" wide ascii nocase
    $o1 = "FontFamilyFromName" wide ascii nocase
    $o2 = "__crtInitCritSecAndSpinCount" wide ascii nocase
  condition:
    3 of ($o*)
}
rule auto_rule_20250726070757_7618 {
  strings:
    $o0 = "pcchValueName" wide ascii nocase
    $o1 = "GetClipboardFormatNameA" wide ascii nocase
    $o2 = "uMsg" wide ascii nocase
    $o3 = "ppsz" wide ascii nocase
    $o4 = "DdeAbandonTransaction" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726070800_7238 {
  strings:
    $o0 = "StrFromTimeIntervalA" wide ascii nocase
    $o1 = "lpszDst" wide ascii nocase
    $o2 = "DdeFreeStringHandle" wide ascii nocase
    $o3 = "VkKeyScanExW" wide ascii nocase
    $o4 = "PathAddBackslashW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726070804_4557 {
  condition:
    auto_rule_20250726070757_7618 or auto_rule_20250726070800_7238
}
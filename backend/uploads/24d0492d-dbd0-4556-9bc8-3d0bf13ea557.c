#include "24d0492d-dbd0-4556-9bc8-3d0bf13ea557.h"

HRESULT __stdcall StringCchCatA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc)
{
  int v3; // edx
  char *v4; // ecx
  HRESULT v5; // esi
  int v6; // esi
  char *i; // eax
  const char *v9; // [esp+0h] [ebp-Ch]
  size_t v10; // [esp+4h] [ebp-8h]

  v5 = 0;
  if ( v3 <= 0 )
    v5 = -2147024809;
  if ( v5 >= 0 )
  {
    v6 = v3;
    for ( i = v4; v6; --v6 )
    {
      if ( !*i )
        break;
      ++i;
    }
    v5 = v6 != 0 ? 0 : -2147024809;
    if ( v5 >= 0 )
      return StringCopyWorkerA(v4, (size_t)pszDest, (size_t *)v4, v9, v10);
  }
  return v5;
}


HRESULT StringCchPrintfA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszFormat, ...)
{
  HRESULT v3; // esi
  size_t v4; // edi
  int v5; // eax
  va_list ArgList; // [esp+18h] [ebp+14h] BYREF

  va_start(ArgList, pszFormat);
  v3 = 0;
  if ( (int)cchDest <= 0 )
    v3 = -2147024809;
  if ( v3 < 0 )
  {
    if ( cchDest )
      *pszDest = 0;
  }
  else
  {
    v3 = 0;
    v4 = cchDest - 1;
    v5 = __vsnprintf(pszDest, cchDest - 1, pszFormat, ArgList);
    if ( v5 < 0 || v5 > v4 )
    {
      v3 = -2147024774;
LABEL_9:
      pszDest[v4] = 0;
      return v3;
    }
    if ( v5 == v4 )
      goto LABEL_9;
  }
  return v3;
}


HRESULT __stdcall StringCopyWorkerA(
        STRSAFE_LPSTR pszDest,
        size_t cchDest,
        size_t *pcchNewDestLength,
        STRSAFE_PCNZCH pszSrc,
        size_t cchToCopy)
{
  int v5; // edx
  _BYTE *v6; // ecx
  int v7; // esi
  size_t v8; // eax
  char v9; // bl

  if ( !v5 )
    goto LABEL_7;
  v7 = 2147483646;
  v8 = cchDest - (_DWORD)v6;
  do
  {
    if ( !v7 )
      break;
    v9 = v6[v8];
    if ( !v9 )
      break;
    *v6++ = v9;
    --v7;
    --v5;
  }
  while ( v5 );
  if ( !v5 )
LABEL_7:
    --v6;
  *v6 = 0;
  return v5 != 0 ? 0 : -2147024774;
}


int __fastcall AvailableBufferCch(unsigned int a1, int a2, unsigned int a3)
{
  if ( a3 < a1 || a3 - a1 > 0x400 )
    return 0;
  else
    return a1 - a3 + 1024;
}


int __thiscall CheckToken(_DWORD *this)
{
  int v2; // ebx
  HMODULE LibraryA; // eax
  HMODULE v4; // edi
  PSID pSid; // [esp+10h] [ebp-14h] BYREF
  BOOL (__stdcall *CheckTokenMembership)(HANDLE, PSID, PBOOL); // [esp+14h] [ebp-10h]
  _SID_IDENTIFIER_AUTHORITY pIdentifierAuthority; // [esp+18h] [ebp-Ch] BYREF

  *(_WORD *)&pIdentifierAuthority.Value[4] = 1280;
  *(_DWORD *)pIdentifierAuthority.Value = 0;
  v2 = 0;
  LibraryA = LoadLibraryA("advapi32.dll");
  v4 = LibraryA;
  if ( LibraryA )
  {
    CheckTokenMembership = (BOOL (__stdcall *)(HANDLE, PSID, PBOOL))GetProcAddress(LibraryA, "CheckTokenMembership");
    if ( CheckTokenMembership )
    {
      *this = 0;
      v2 = 1;
      if ( AllocateAndInitializeSid(&pIdentifierAuthority, 2u, 0x20u, 0x220u, 0, 0, 0, 0, 0, 0, &pSid) )
      {
        ((void (__thiscall *)(BOOL (__stdcall *)(HANDLE, PSID, PBOOL), _DWORD, PSID, _DWORD *))CheckTokenMembership)(
          CheckTokenMembership,
          0,
          pSid,
          this);
        FreeSid(pSid);
      }
    }
    FreeLibrary(v4);
  }
  return v2;
}


BOOL __stdcall IsNTAdmin(DWORD dwReserved, DWORD *lpdwReserved)
{
  BOOL result; // eax
  unsigned int v3; // ebx
  HANDLE CurrentProcess; // eax
  PSID *v5; // esi
  PSID *v6; // edi
  PSID pSid; // [esp+8h] [ebp-1Ch] BYREF
  HANDLE TokenHandle; // [esp+Ch] [ebp-18h] BYREF
  DWORD ReturnLength; // [esp+10h] [ebp-14h] BYREF
  BOOL v10; // [esp+14h] [ebp-10h] BYREF
  struct _SID_IDENTIFIER_AUTHORITY pIdentifierAuthority; // [esp+18h] [ebp-Ch] BYREF

  result = dword_408128;
  v3 = 0;
  *(_WORD *)&pIdentifierAuthority.Value[4] = 1280;
  *(_DWORD *)pIdentifierAuthority.Value = 0;
  v10 = 0;
  if ( dword_408128 == 2 )
  {
    if ( CheckToken(&v10) )
    {
      result = v10;
      if ( v10 )
        dword_408128 = 1;
    }
    else
    {
      CurrentProcess = GetCurrentProcess();
      result = OpenProcessToken(CurrentProcess, 8u, &TokenHandle);
      if ( result )
      {
        if ( !GetTokenInformation(TokenHandle, TokenGroups, 0, 0, &ReturnLength) && GetLastError() == 122 )
        {
          v5 = (PSID *)LocalAlloc(0, ReturnLength);
          if ( v5 )
          {
            if ( GetTokenInformation(TokenHandle, TokenGroups, v5, ReturnLength, &ReturnLength)
              && AllocateAndInitializeSid(&pIdentifierAuthority, 2u, 0x20u, 0x220u, 0, 0, 0, 0, 0, 0, &pSid) )
            {
              if ( *v5 )
              {
                v6 = v5 + 1;
                while ( !EqualSid(*v6, pSid) )
                {
                  ++v3;
                  v6 += 2;
                  if ( v3 >= (unsigned int)*v5 )
                    goto LABEL_15;
                }
                dword_408128 = 1;
                v10 = 1;
              }
LABEL_15:
              FreeSid(pSid);
            }
            LocalFree(v5);
          }
        }
        CloseHandle(TokenHandle);
        return v10;
      }
    }
  }
  return result;
}


int __stdcall WarningDlgProc(HWND hDlg, int a2, INT_PTR nResult, UINT uID)
{
  HWND DesktopWindow; // eax
  CHAR Buffer[512]; // [esp+4h] [ebp-204h] BYREF

  if ( a2 == 272 )
  {
    DesktopWindow = GetDesktopWindow();
    CenterWindow(hDlg, DesktopWindow);
    Buffer[0] = 0;
    LoadStringA(g_hInst, uID, Buffer, 512);
    SetDlgItemTextA(hDlg, 2111, Buffer);
    MessageBeep(0xFFFFFFFF);
  }
  else
  {
    if ( a2 != 273 || (unsigned int)(nResult - 2109) > 1 )
      return 0;
    EndDialog(hDlg, nResult);
  }
  return 1;
}


_BYTE *__fastcall ExtractField(_BYTE **a1, const CHAR *a2)
{
  int v3; // edi
  _BYTE *v4; // esi
  _BYTE *result; // eax

  v3 = 0;
  v4 = *a1;
  while ( ANSIStrChr(a2) )
  {
    if ( !*v4 )
      return 0;
    ++v4;
  }
  *a1 = v4;
  while ( !ANSIStrChr(a2) && v4[v3] )
    ++v3;
  result = &v4[v3];
  if ( v4[v3] )
    *result++ = 0;
  return result;
}


int __thiscall AnalyzeCmd(STRSAFE_LPSTR pszDest, char **a2, _DWORD *a3)
{
  const CHAR *v4; // edx
  char *v5; // eax
  char *v6; // eax
  char *v7; // ecx
  char *v8; // esi
  char *v9; // edi
  char v10; // al
  const CHAR *v11; // eax
  DWORD FileAttributesA; // eax
  char *v13; // eax
  char *v14; // esi
  STRSAFE_LPSTR v15; // edi
  const CHAR *v16; // eax
  const char *v17; // ebx
  int result; // eax
  const CHAR *v19; // eax
  SIZE_T v20; // edi
  DWORD v21; // eax
  char *v22; // ecx
  size_t v23; // [esp+0h] [ebp-624h]
  const char *v24; // [esp+0h] [ebp-624h]
  const char *v25; // [esp+0h] [ebp-624h]
  size_t v26; // [esp+0h] [ebp-624h]
  size_t v27; // [esp+0h] [ebp-624h]
  size_t v28; // [esp+0h] [ebp-624h]
  const char *v29; // [esp+4h] [ebp-620h]
  const char *v30; // [esp+4h] [ebp-620h]
  const char *v31; // [esp+4h] [ebp-620h]
  STRSAFE_LPCSTR v32; // [esp+4h] [ebp-620h]
  const char *v33; // [esp+4h] [ebp-620h]
  STRSAFE_LPCSTR v34; // [esp+4h] [ebp-620h]
  STRSAFE_LPSTR pszDesta; // [esp+14h] [ebp-610h] BYREF
  CHAR sz[1024]; // [esp+18h] [ebp-60Ch] BYREF
  char v37; // [esp+418h] [ebp-20Ch] BYREF
  char v38; // [esp+419h] [ebp-20Bh] BYREF
  CHAR FileName[260]; // [esp+51Ch] [ebp-108h] BYREF

  StringCchCopyA(pszDest, v23, v29);
  if ( v37 == 34 )
  {
    v4 = "\"";
    v5 = &v38;
  }
  else
  {
    v4 = " ";
    v5 = &v37;
  }
  pszDesta = v5;
  v6 = ExtractField(&pszDesta, v4);
  v8 = pszDesta;
  v9 = v6;
  if ( pszDesta
    && (v7 = (char *)strlen(pszDesta), (unsigned int)v7 >= 3)
    && ((v10 = pszDesta[1], v10 == 58) && pszDesta[2] == 92 || *pszDesta == 92 && v10 == 92) )
  {
    StringCchCopyA(pszDesta, (size_t)v24, v30);
  }
  else
  {
    StringCopyWorkerA(v7, (size_t)&PathName, (size_t *)v7, v24, (size_t)v30);
    AddPath(FileName, v8);
  }
  v11 = (const CHAR *)ANSIStrRChr(v8);
  if ( v11 && CompareStringA(0x7Fu, 1u, v11, -1, ".INF", -1) == 2 )
  {
    FileAttributesA = GetFileAttributesA(FileName);
    if ( FileAttributesA == -1 || (FileAttributesA & 0x10) != 0 )
    {
      MsgBox2Param(0, 1317, FileName, 0, 16, 0);
      return 0;
    }
    pszDesta = v9;
    v13 = ExtractField(&pszDesta, "[");
    if ( v13 )
    {
      if ( *v13 )
        pszDesta = v13;
      ExtractField(&pszDesta, "]");
    }
    v14 = (char *)LocalAlloc(0x40u, 0x200u);
    if ( v14 )
    {
      v15 = pszDesta;
      v16 = pszDesta;
      if ( !*pszDesta )
        v16 = aDefaultinstall;
      g_uInfRebootOn = GetPrivateProfileIntA(v16, "Reboot", 0, FileName);
      *a3 = 1;
      if ( GetPrivateProfileStringA("Version", "AdvancedINF", pszCabPath, v14, 8u, FileName) )
      {
        dword_409A34 |= 4u;
        if ( !*v15 )
          v15 = aDefaultinstall;
        StringCchCopyA(v15, (size_t)v25, v31);
        StringCchCopyA(FileName, v26, v32);
      }
      else
      {
        dword_409A34 &= ~4u;
        if ( g_wOSVer )
        {
          v17 = "setupapi.dll";
        }
        else
        {
          v17 = "setupx.dll";
          GetShortPathNameA(FileName, FileName, 0x104u);
        }
        if ( !*v15 )
          v15 = aDefaultinstall;
        StringCchPrintfA(v14, 0x200u, "rundll32.exe %s,InstallHinfSection %s 128 %s", v17, v15, FileName);
      }
      goto LABEL_48;
    }
    goto LABEL_38;
  }
  v19 = (const CHAR *)ANSIStrRChr(v8);
  if ( !v19 || CompareStringA(0x7Fu, 1u, v19, -1, ".BAT", -1) != 2 )
  {
    v14 = (char *)LocalAlloc(0x40u, 0x400u);
    if ( v14 )
    {
      v21 = GetFileAttributesA(FileName);
      if ( v21 == -1 || (v21 & 0x10) != 0 )
      {
        StringCchCopyA(pszDest, (size_t)v25, v31);
      }
      else
      {
        StringCopyWorkerA(v22, (size_t)FileName, (size_t *)v22, v25, (size_t)v31);
        if ( v9 && *v9 )
        {
          StringCchCatA((STRSAFE_LPSTR)" ", v27, v33);
          StringCchCatA(v9, v28, v34);
        }
      }
      *v14 = 0;
      ExpandCmdParams(sz, v14);
      goto LABEL_48;
    }
    goto LABEL_38;
  }
  v20 = strlen(FileName) + strlen(aCommandComCS) + 8;
  v14 = (char *)LocalAlloc(0x40u, v20);
  if ( !v14 )
  {
LABEL_38:
    MsgBox2Param(0, 1205, 0, 0, 16, 0);
    return 0;
  }
  StringCchPrintfA(v14, v20, "Command.com /c %s", FileName);
LABEL_48:
  result = 1;
  *a2 = v14;
  return result;
}


int __stdcall CheckReboot()
{
  int v0; // edi
  int v1; // esi

  v0 = -1;
  if ( g_uInfRebootOn )
    return 2;
  v1 = g_dwRebootCheck;
  if ( v1 != NeedRebootInit() )
    return 2;
  return v0;
}


int __stdcall MyNTReboot()
{
  HANDLE CurrentProcess; // eax
  int v1; // edx
  BOOL v3; // esi
  HANDLE TokenHandle; // [esp+4h] [ebp-18h] BYREF
  _TOKEN_PRIVILEGES NewState; // [esp+8h] [ebp-14h] BYREF

  CurrentProcess = GetCurrentProcess();
  if ( !OpenProcessToken(CurrentProcess, 0x28u, &TokenHandle) )
  {
    v1 = 1269;
LABEL_3:
    MsgBox2Param(0, v1, 0, 0, 16, 0);
    return 0;
  }
  LookupPrivilegeValueA(0, "SeShutdownPrivilege", &NewState.Privileges[0].Luid);
  NewState.PrivilegeCount = 1;
  NewState.Privileges[0].Attributes = 2;
  v3 = AdjustTokenPrivileges(TokenHandle, 0, &NewState, 0, 0, 0);
  CloseHandle(TokenHandle);
  if ( !v3 )
  {
    v1 = 1270;
    goto LABEL_3;
  }
  if ( !ExitWindowsEx(2u, 0) )
  {
    v1 = 1271;
    goto LABEL_3;
  }
  return 1;
}


int __fastcall MyRestartDialog(char a1)
{
  int result; // eax

  if ( (a1 & 2) != 0 || (result = CheckReboot(), result == 2) )
  {
    if ( (a1 & 4) != 0 || (result = MsgBox2Param(0, 1314, pszCabPath, 0, 64, 4), result == 6) )
    {
      if ( g_wOSVer )
        return MyNTReboot();
      else
        return ExitWindowsEx(2u, 0);
    }
  }
  return result;
}


void __thiscall CleanRegRunOnce(HKEY this)
{
  HKEY phkResult; // [esp+0h] [ebp-4h] BYREF

  phkResult = this;
  if ( g_szRegValName )
  {
    if ( !RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x20006u, &phkResult) )
    {
      RegDeleteValueA(phkResult, &g_szRegValName);
      RegCloseKey(phkResult);
    }
  }
}


HLOCAL __stdcall AddRegRunOnce()
{
  BOOL v0; // ebx
  HLOCAL result; // eax
  int i; // esi
  HMODULE LibraryA; // eax
  HMODULE v4; // edi
  FARPROC DelNodeRunDLL32; // esi
  unsigned int v6; // kr00_4
  unsigned int v7; // kr04_4
  char *v8; // esi
  const char *v9; // eax
  DWORD cbData; // [esp+8h] [ebp-218h] BYREF
  DWORD dwDisposition; // [esp+Ch] [ebp-214h] BYREF
  HKEY phkResult; // [esp+10h] [ebp-210h] BYREF
  CHAR Buffer[260]; // [esp+14h] [ebp-20Ch] BYREF
  CHAR Filename[260]; // [esp+118h] [ebp-108h] BYREF

  memset(Filename, 0, sizeof(Filename));
  memset(Buffer, 0, sizeof(Buffer));
  v0 = 0;
  result = (HLOCAL)RegCreateKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0, 0, 0x2001Fu, 0, &phkResult, &dwDisposition);
  if ( !result )
  {
    for ( i = 0; i < 200; ++i )
    {
      StringCchPrintfA(&g_szRegValName, 0x50u, "wextract_cleanup%d", i);
      if ( RegQueryValueExA(phkResult, &g_szRegValName, 0, 0, 0, &cbData) )
        break;
    }
    if ( i == 200 )
    {
      result = (HLOCAL)RegCloseKey(phkResult);
      g_szRegValName = 0;
      return result;
    }
    GetSystemDirectoryA(Buffer, 0x104u);
    AddPath(Buffer, (STRSAFE_LPSTR)"advpack.dll");
    LibraryA = LoadLibraryA(Buffer);
    v4 = LibraryA;
    if ( LibraryA
      && (DelNodeRunDLL32 = GetProcAddress(LibraryA, "DelNodeRunDLL32"),
          v0 = DelNodeRunDLL32 != 0,
          FreeLibrary(v4),
          DelNodeRunDLL32) )
    {
      if ( GetSystemDirectoryA(Filename, 0x104u) )
        AddPath(Filename, (STRSAFE_LPSTR)pszCabPath);
    }
    else if ( !GetModuleFileNameA(g_hInst, Filename, 0x104u) )
    {
      return (HLOCAL)RegCloseKey(phkResult);
    }
    v6 = strlen(Filename);
    v7 = strlen(&PathName);
    v8 = (char *)LocalAlloc(0x40u, v7 + v6 + 80);
    if ( !v8 )
    {
      MsgBox2Param(0, 1205, 0, 0, 16, 0);
      return (HLOCAL)RegCloseKey(phkResult);
    }
    g_bConvertRunOnce = !v0;
    v9 = aRundll32ExeSad;
    if ( !v0 )
      v9 = aSDS;
    StringCchPrintfA(v8, v7 + v6 + 80, v9, Filename, &PathName);
    RegSetValueExA(phkResult, &g_szRegValName, 0, 1u, (const BYTE *)v8, strlen(v8) + 1);
    RegCloseKey(phkResult);
    return LocalFree(v8);
  }
  return result;
}


void __stdcall ConvertRegRunOnce()
{
  DWORD cbData; // [esp+0h] [ebp-348h] BYREF
  HKEY phkResult; // [esp+4h] [ebp-344h] BYREF
  BYTE Data[568]; // [esp+8h] [ebp-340h] BYREF
  CHAR Buffer[260]; // [esp+240h] [ebp-108h] BYREF

  if ( g_szRegValName && !RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x2001Fu, &phkResult) )
  {
    cbData = 568;
    if ( !RegQueryValueExA(phkResult, &g_szRegValName, 0, 0, Data, &cbData) )
    {
      memset(Buffer, 0, sizeof(Buffer));
      if ( GetSystemDirectoryA(Buffer, 0x104u) )
        AddPath(Buffer, (STRSAFE_LPSTR)pszCabPath);
      StringCchPrintfA(
        (STRSAFE_LPSTR)Data,
        0x238u,
        "rundll32.exe %sadvpack.dll,DelNodeRunDLL32 \"%s\"",
        Buffer,
        &PathName);
      RegSetValueExA(phkResult, &g_szRegValName, 0, 1u, Data, strlen((const char *)Data) + 1);
    }
    RegCloseKey(phkResult);
  }
}


void __thiscall DeleteMyDir(char *this)
{
  HANDLE FirstFileA; // edi
  size_t v3; // [esp+0h] [ebp-260h]
  size_t v4; // [esp+0h] [ebp-260h]
  size_t v5; // [esp+0h] [ebp-260h]
  const char *v6; // [esp+4h] [ebp-25Ch]
  STRSAFE_LPCSTR v7; // [esp+4h] [ebp-25Ch]
  const char *v8; // [esp+4h] [ebp-25Ch]
  _WIN32_FIND_DATAA FindFileData; // [esp+10h] [ebp-250h] BYREF
  char pszDest[268]; // [esp+150h] [ebp-110h] BYREF

  if ( this )
  {
    if ( *this )
    {
      StringCchCopyA(this, v3, v6);
      StringCchCatA((STRSAFE_LPSTR)"*", v4, v7);
      FirstFileA = FindFirstFileA(pszDest, &FindFileData);
      if ( FirstFileA != (HANDLE)-1 )
      {
        do
        {
          StringCchCopyA(this, v5, v8);
          if ( (FindFileData.dwFileAttributes & 0x10) != 0 )
          {
            if ( lstrcmpA(FindFileData.cFileName, ".") )
            {
              if ( lstrcmpA(FindFileData.cFileName, "..") )
              {
                StringCchCatA(FindFileData.cFileName, v5, v8);
                AddPath(pszDest, (STRSAFE_LPSTR)pszCabPath);
                DeleteMyDir(pszDest);
              }
            }
          }
          else
          {
            StringCchCatA(FindFileData.cFileName, v5, v8);
            SetFileAttributesA(pszDest, 0x80u);
            DeleteFileA(pszDest);
          }
        }
        while ( FindNextFileA(FirstFileA, &FindFileData) );
        FindClose(FirstFileA);
        RemoveDirectoryA(this);
      }
    }
  }
}


LONG __stdcall GetWininitSize()
{
  LONG v0; // esi
  HFILE v1; // eax
  HFILE v2; // edi
  CHAR Buffer[260]; // [esp+8h] [ebp-108h] BYREF

  v0 = 0;
  if ( GetWindowsDirectoryA(Buffer, 0x104u) )
  {
    AddPath(Buffer, (STRSAFE_LPSTR)"wininit.ini");
    WritePrivateProfileStringA(0, 0, 0, Buffer);
    v1 = _lopen(Buffer, 64);
    v2 = v1;
    if ( v1 != -1 )
    {
      v0 = _llseek(v1, 0, 2);
      _lclose(v2);
    }
  }
  return v0;
}


DWORD __stdcall NeedRebootInit()
{
  unsigned __int16 v0; // cx
  DWORD v1; // esi
  LSTATUS v2; // eax
  HKEY phkResult; // [esp+4h] [ebp-8h] BYREF
  DWORD cbData; // [esp+8h] [ebp-4h] BYREF

  v1 = 0;
  if ( !v0 )
    return GetWininitSize();
  if ( v0 == 1 )
  {
    cbData = 0;
    if ( RegOpenKeyExA(HKEY_LOCAL_MACHINE, aSystemCurrentc_0, 0, 0x20019u, &phkResult) )
      return cbData;
    v2 = RegQueryInfoKeyA(phkResult, 0, 0, 0, 0, 0, 0, &cbData, 0, 0, 0, 0);
    goto LABEL_6;
  }
  if ( v0 <= 3u )
  {
    cbData = 0;
    if ( RegOpenKeyExA(HKEY_LOCAL_MACHINE, aSystemCurrentc, 0, 0x20019u, &phkResult) )
      return cbData;
    v2 = RegQueryValueExA(phkResult, ValueName, 0, 0, 0, &cbData);
LABEL_6:
    cbData &= -(v2 == 0);
    RegCloseKey(phkResult);
    return cbData;
  }
  return v1;
}


BOOL __thiscall IsWindowsDrive(_BYTE *this)
{
  CHAR Buffer[260]; // [esp+4h] [ebp-108h] BYREF

  if ( !GetWindowsDirectoryA(Buffer, 0x104u) )
    MsgBox2Param(0, 1264, 0, 0, 16, 0);
  return *this == Buffer[0];
}


BOOL __fastcall DiskSpaceErrMsg(int a1, int a2, int a3, int a4)
{
  int v4; // esi
  char pszDest[12]; // [esp+Ch] [ebp-10h] BYREF

  g_dwExitCode = 112;
  v4 = 0;
  switch ( a1 )
  {
    case 1:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a2 + a3);
      MsgBox2Param(0, 1274, pszDest, 0, 16, 0);
      break;
    case 4:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a2 + a3);
      return MsgBox2Param(0, 1213, pszDest, 0, 32, 5) == 4;
    case 2:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a3);
      if ( MsgBox2Param(0, 1228, pszDest, a4, 64, 260) == 6 )
      {
        g_dwExitCode = 0;
        return 1;
      }
      break;
  }
  return v4;
}


int __thiscall GetFileTobeChecked(CHAR *lpszStart, int a2)
{
  int v2; // ebx
  const CHAR *v4; // eax
  char *v5; // ecx
  DWORD v6; // eax
  const char *v8; // [esp+0h] [ebp-128h]
  size_t v9; // [esp+0h] [ebp-128h]
  size_t v10; // [esp+4h] [ebp-124h]
  const char *v11; // [esp+4h] [ebp-124h]
  DWORD cbData; // [esp+Ch] [ebp-11Ch] BYREF
  HKEY phkResult; // [esp+10h] [ebp-118h] BYREF
  DWORD Type; // [esp+14h] [ebp-114h] BYREF
  STRSAFE_LPSTR pszDest; // [esp+18h] [ebp-110h]
  unsigned __int8 v16; // [esp+1Fh] [ebp-109h]
  CHAR SubKey[260]; // [esp+20h] [ebp-108h] BYREF

  v2 = 0;
  pszDest = (STRSAFE_LPSTR)a2;
  *lpszStart = 0;
  if ( *(_BYTE *)a2 == 35 )
  {
    v16 = (unsigned __int8)CharUpperA((LPSTR)*(char *)(a2 + 1));
    v4 = CharNextA((LPCSTR)(a2 + 1));
    pszDest = CharNextA(v4);
    if ( v16 != 83 )
    {
      if ( v16 == 87 )
      {
        GetWindowsDirectoryA(lpszStart, 0x104u);
      }
      else
      {
        cbData = 260;
        StringCopyWorkerA(v5, (size_t)"Software\\Microsoft\\Windows\\CurrentVersion\\App Paths", (size_t *)v5, v8, v10);
        AddPath(SubKey, pszDest);
        if ( !RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x20019u, &phkResult) )
        {
          if ( !RegQueryValueExA(phkResult, pszCabPath, 0, &Type, (LPBYTE)lpszStart, &cbData) )
          {
            v6 = Type;
            if ( Type == 2 )
            {
              if ( ExpandEnvironmentStringsA(lpszStart, SubKey, 0x104u) )
              {
                StringCchCopyA(SubKey, v9, v11);
LABEL_11:
                v2 = 1;
                goto LABEL_12;
              }
              v6 = Type;
            }
            if ( v6 == 1 )
              goto LABEL_11;
          }
LABEL_12:
          RegCloseKey(phkResult);
          goto LABEL_15;
        }
      }
LABEL_16:
      AddPath(lpszStart, pszDest);
      return 1;
    }
  }
  GetSystemDirectoryA(lpszStart, 0x104u);
LABEL_15:
  if ( !v2 )
    goto LABEL_16;
  return 1;
}


int __fastcall CheckFileVersion(int a1, const CHAR *a2, int a3, _DWORD *a4)
{
  int v4; // edx
  int v5; // esi
  int v6; // ebx
  void *v7; // edi
  int v8; // eax
  DWORD FileVersionInfoSizeA; // eax
  HGLOBAL v10; // eax
  void *v11; // eax
  int v12; // ebx
  int v13; // eax
  int *v14; // esi
  int v15; // eax
  int v17; // [esp-4h] [ebp-4Ch]
  _DWORD v18[2]; // [esp+Ch] [ebp-3Ch]
  _DWORD v19[3]; // [esp+14h] [ebp-34h]
  LPVOID lpBuffer; // [esp+20h] [ebp-28h] BYREF
  unsigned int puLen; // [esp+24h] [ebp-24h] BYREF
  LPCVOID pBlock; // [esp+28h] [ebp-20h]
  DWORD dwHandle; // [esp+2Ch] [ebp-1Ch] BYREF
  DWORD dwLen; // [esp+30h] [ebp-18h]
  int v25; // [esp+34h] [ebp-14h]
  int v26; // [esp+38h] [ebp-10h]
  int v27; // [esp+3Ch] [ebp-Ch]
  LPCSTR lptstrFilename; // [esp+40h] [ebp-8h]
  int v29; // [esp+44h] [ebp-4h]

  lptstrFilename = a2;
  v4 = a1;
  v5 = 0;
  v27 = a1;
  v6 = 0;
  v7 = 0;
  v26 = 0;
  if ( *(int *)(a1 + 124) <= 0 )
  {
LABEL_20:
    v5 = 1;
  }
  else
  {
    v8 = 0;
    v29 = 0;
    while ( 1 )
    {
      v25 = *(_DWORD *)(v4 + 128);
      if ( !GetFileTobeChecked((CHAR *)lptstrFilename, v4 + 132 + *(_DWORD *)(v4 + v8 + v25 + 188)) )
        break;
      FileVersionInfoSizeA = GetFileVersionInfoSizeA(lptstrFilename, &dwHandle);
      dwLen = FileVersionInfoSizeA;
      if ( FileVersionInfoSizeA )
      {
        v10 = GlobalAlloc(0x42u, FileVersionInfoSizeA);
        v7 = v10;
        if ( !v10 )
          break;
        v11 = GlobalLock(v10);
        pBlock = v11;
        if ( !v11 )
          break;
        if ( GetFileVersionInfoA(lptstrFilename, dwHandle, dwLen, v11) )
        {
          if ( VerQueryValueA(pBlock, "\\", &lpBuffer, &puLen) )
          {
            if ( puLen )
            {
              v12 = 0;
              v13 = *((_DWORD *)lpBuffer + 2);
              dwLen = *((_DWORD *)lpBuffer + 3);
              v19[2] = v13;
              pBlock = (LPCVOID)(v25 + 148 + v27 + v29);
              v14 = (int *)pBlock;
              do
              {
                v15 = CompareVersion(*(v14 - 4), *(v14 - 3));
                v17 = *v14;
                v19[v12] = v15;
                v18[v12] = CompareVersion(*(v14 - 1), v17);
                v14 += 6;
                ++v12;
              }
              while ( v12 < 2 );
              v6 = v26;
              v5 = 0;
              if ( (v19[0] < 0 || v18[0] > 0) && (v19[1] < 0 || v18[1] > 0) )
              {
                GlobalUnlock(v7);
                break;
              }
            }
          }
        }
        GlobalUnlock(v7);
        v4 = v27;
      }
      else
      {
        v4 = v27;
        v6 = v26;
        if ( *(_DWORD *)(v27 + v29 + v25 + 132) || *(_DWORD *)(v27 + v29 + v25 + 136) )
          break;
      }
      ++v6;
      v8 = v29 + 60;
      v26 = v6;
      v29 += 60;
      if ( v6 >= *(_DWORD *)(v4 + 124) )
        goto LABEL_20;
    }
  }
  *a4 = v6;
  if ( v7 )
    GlobalFree(v7);
  return v5;
}


int __fastcall CompareVersion(unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
  if ( a1 >= a3 )
  {
    if ( a1 > a3 )
      return 1;
    if ( a2 >= a4 )
      return a2 > a4;
  }
  return -1;
}


void __fastcall ExpandCmdParams(BYTE *lpsz, unsigned int a2, CHAR *lpsza)
{
  BYTE *v5; // edi
  BOOL v6; // eax
  LPSTR v7; // eax
  int v8; // edx
  size_t v9; // [esp+0h] [ebp-114h]
  const char *v10; // [esp+4h] [ebp-110h]
  CHAR Filename[260]; // [esp+Ch] [ebp-108h] BYREF

  v5 = lpsz;
  if ( *lpsz )
  {
    GetModuleFileNameA(g_hInst, Filename, 0x104u);
    while ( 1 )
    {
      if ( !*v5 )
      {
        *lpsza = 0;
        return;
      }
      v6 = IsDBCSLeadByte(*v5);
      *lpsza = *v5;
      if ( v6 )
        lpsza[1] = v5[1];
      if ( *v5 != 35 )
        goto LABEL_14;
      v5 = (BYTE *)CharNextA((LPCSTR)v5);
      if ( (unsigned __int8)CharUpperA((LPSTR)(char)*v5) == 68 )
      {
        GetParentDir(Filename);
        v7 = CharPrevA(Filename, &Filename[strlen(Filename)]);
        if ( v7 )
        {
          if ( *v7 == 92 )
            *v7 = 0;
        }
LABEL_12:
        AvailableBufferCch(a2, v8, (unsigned int)lpsza);
        StringCchCopyA(Filename, v9, v10);
        lpsza += strlen(lpsza);
        goto LABEL_15;
      }
      if ( (unsigned __int8)CharUpperA((LPSTR)(char)*v5) == 69 )
        goto LABEL_12;
      if ( *v5 == 35 )
LABEL_14:
        lpsza = CharNextA(lpsza);
LABEL_15:
      v5 = (BYTE *)CharNextA((LPCSTR)v5);
    }
  }
}


int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
  signed int Version; // eax
  int v5; // ecx
  HMODULE ModuleHandleW; // eax
  BOOL (__stdcall *HeapSetInformation)(HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T); // eax
  int v8; // esi

  Version = GetVersion();
  if ( Version >= 0 && (unsigned __int8)Version >= 6u )
  {
    ModuleHandleW = GetModuleHandleW(L"Kernel32.dll");
    if ( ModuleHandleW )
    {
      HeapSetInformation = (BOOL (__stdcall *)(HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T))GetProcAddress(
                                                                                                ModuleHandleW,
                                                                                                "HeapSetInformation");
      if ( HeapSetInformation )
        ((void (__thiscall *)(BOOL (__stdcall *)(HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T), _DWORD, int, _DWORD, _DWORD))HeapSetInformation)(
          HeapSetInformation,
          0,
          1,
          0,
          0);
    }
  }
  g_dwExitCode = 0;
  if ( Init(hInstance, lpCmdLine, v5) )
  {
    v8 = DoMain();
    DeleteExtractedFiles();
    if ( v8 )
    {
      if ( !byte_408A3A && (dword_409A2C & 1) != 0 )
        MyRestartDialog(dword_409A2C);
    }
  }
  if ( g_hMutex )
    CloseHandle(g_hMutex);
  return g_dwExitCode;
}


int __fastcall Init(HMODULE hModule, LPCSTR lpsz, int a3)
{
  HGLOBAL v3; // edi
  unsigned int Resource; // eax
  int v7; // edx
  HRSRC ResourceA; // eax
  DWORD v10; // [esp+0h] [ebp-114h]
  DWORD *v11; // [esp+4h] [ebp-110h]
  CHAR Name[260]; // [esp+Ch] [ebp-108h] BYREF

  v3 = 0;
  g_hInst = hModule;
  memset(&g_Sess, 0, 0x8FCu);
  memset(&g_CMD, 0, 0x32Cu);
  memset(&g_szBrowsePath, 0, 0x104u);
  dword_4093EC = 1;
  Resource = GetResource("TITLE", Destination, 0x7Fu);
  if ( !Resource || Resource > 0x80 )
  {
    v7 = 1201;
    goto LABEL_33;
  }
  g_hCancelEvent = CreateEventA(0, 1, 1, 0);
  SetEvent(g_hCancelEvent);
  if ( !GetResource("EXTRACTOPT", &dword_409A34, 4u) )
  {
LABEL_4:
    MsgBox2Param(0, 1201, 0, 0, 16, 0);
    g_dwExitCode = -2147023084;
    return 0;
  }
  if ( (dword_409A34 & 0xC0) != 0 )
  {
    if ( !GetResource("INSTANCECHECK", Name, 0x104u) )
      goto LABEL_4;
    g_hMutex = CreateMutexA(0, 1, Name);
    if ( g_hMutex )
    {
      if ( GetLastError() == 183 )
      {
        if ( (dword_409A34 & 0x80u) != 0 )
        {
          MsgBox2Param(0, 1355, Destination, 0, 16, 0);
LABEL_12:
          CloseHandle(g_hMutex);
          g_dwExitCode = -2147024713;
          return 0;
        }
        if ( MsgBox2Param(0, 1316, Destination, 0, 32, 4) != 6 )
          goto LABEL_12;
      }
    }
  }
  g_uInfRebootOn = 0;
  if ( !ParseCmdLine(lpsz) )
  {
    v7 = 1312;
LABEL_33:
    MsgBox2Param(0, v7, 0, 0, 16, 0);
    return 0;
  }
  if ( byte_408A3A )
  {
    DeleteMyDir(&byte_408A3A);
  }
  else
  {
    ResourceA = FindResourceA(hModule, "VERCHECK", (LPCSTR)0xA);
    if ( ResourceA )
      v3 = LoadResource(hModule, ResourceA);
    if ( g_fOSSupportsFullUI )
      InitCommonControls();
    if ( dword_408A24 )
      return 1;
    if ( CheckOSVersion(v3)
      && (g_wOSVer != 1 && g_wOSVer != 2 && g_wOSVer != 3
       || (dword_409A34 & 0x100) == 0
       || (word_408A38 & 1) != 0
       || IsNTAdmin(v10, v11)
       || MyDialogBox(0, WarningDlgProc, 1351, 2110) == 2109) )
    {
      return 1;
    }
  }
  return 0;
}


int __stdcall DoMain()
{
  HMODULE LibraryA; // eax
  HMODULE v1; // ebx
  DWORD v2; // edi
  BOOL (__stdcall *DecryptFileA)(LPCSTR, DWORD); // eax
  int v5; // eax
  CHAR Buffer[264]; // [esp+10h] [ebp-10Ch] BYREF

  if ( word_408A38 )
    goto LABEL_6;
  if ( !dword_408A24 )
  {
    if ( !GetUsersPermission() )
      return 0;
    if ( word_408A38 )
      goto LABEL_6;
  }
  if ( !DisplayLicense() )
    return 0;
LABEL_6:
  if ( !GetFileList() || !GetTempDirectory() )
    return 0;
  GetSystemDirectoryA(Buffer, 0x105u);
  AddPath(Buffer, (STRSAFE_LPSTR)"advapi32.dll");
  LibraryA = LoadLibraryA(Buffer);
  v1 = LibraryA;
  v2 = 0;
  if ( LibraryA )
  {
    DecryptFileA = (BOOL (__stdcall *)(LPCSTR, DWORD))GetProcAddress(LibraryA, "DecryptFileA");
    if ( DecryptFileA )
      ((void (__thiscall *)(BOOL (__stdcall *)(LPCSTR, DWORD), CHAR *, _DWORD))DecryptFileA)(DecryptFileA, &PathName, 0);
  }
  FreeLibrary(v1);
  if ( !dword_408A24 && !dword_409A30 && !CheckWinDir() )
    return 0;
  if ( !SetCurrentDirectoryA(&PathName) )
  {
    MsgBox2Param(0, 1212, 0, 0, 16, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  if ( !dword_408A2C && !ExtractFiles() )
    return 0;
  if ( (dword_408D48 & 0xC0) == 0 )
    v2 = NeedRebootInit();
  v5 = dword_408A24;
  g_dwRebootCheck = v2;
  if ( !dword_408A24 && !dword_409A30 )
  {
    if ( !RunInstallCommand() )
      return 0;
    v5 = dword_408A24;
  }
  if ( !word_408A38 && !v5 )
    FinishMessage();
  return 1;
}


LRESULT __stdcall MEditSubProc(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam)
{
  if ( Msg == 177 && !wParam && lParam == -2 )
    return 0;
  else
    return CallWindowProcA(g_lpfnOldMEditWndProc, hWnd, Msg, wParam, lParam);
}


int __stdcall LicenseDlgProc(HWND hDlg, int a2, int a3, int a4)
{
  HWND DesktopWindow; // eax
  HWND DlgItem; // esi

  switch ( a2 )
  {
    case 15:
      if ( !dword_408590 )
      {
        SendDlgItemMessageA(hDlg, 2100, 0xB1u, 0xFFFFFFFF, 0);
        dword_408590 = 1;
      }
      break;
    case 16:
      goto LABEL_8;
    case 272:
      DesktopWindow = GetDesktopWindow();
      CenterWindow(hDlg, DesktopWindow);
      SetDlgItemTextA(hDlg, 2100, g_szLicense);
      SetWindowTextA(hDlg, Destination);
      SetForegroundWindow(hDlg);
      DlgItem = GetDlgItem(hDlg, 2100);
      g_lpfnOldMEditWndProc = (WNDPROC)GetWindowLongA(DlgItem, -4);
      SetWindowLongA(DlgItem, -4, (LONG)MEditSubProc);
      return 1;
    case 273:
      if ( a3 == 6 )
      {
        EndDialog(hDlg, 1);
        return 1;
      }
      if ( a3 != 7 )
        return 1;
LABEL_8:
      EndDialog(hDlg, 0);
      return 1;
  }
  return 0;
}


BOOL __thiscall IsFullPath(int this)
{
  BOOL result; // eax
  char v2; // al

  result = 0;
  if ( strlen((const char *)this) >= 3 )
  {
    v2 = *(_BYTE *)(this + 1);
    if ( v2 == 58 || *(_BYTE *)this == 92 && v2 == 92 )
      return 1;
  }
  return result;
}


int __stdcall TempDirDlgProc(HWND hDlg, int a2, int a3, int a4)
{
  int v5; // ecx
  int v6; // edx
  HWND DesktopWindow; // eax
  HWND DlgItem; // eax

  if ( a2 == 16 )
  {
    EndDialog(hDlg, 0);
    return 1;
  }
  if ( a2 == 272 )
  {
    DesktopWindow = GetDesktopWindow();
    CenterWindow(hDlg, DesktopWindow);
    SetWindowTextA(hDlg, Destination);
    SendDlgItemMessageA(hDlg, 2101, 0xC5u, 0x103u, 0);
    if ( g_wOSVer == 1 )
    {
      DlgItem = GetDlgItem(hDlg, 2102);
      EnableWindow(DlgItem, 0);
    }
    return 1;
  }
  if ( a2 != 273 )
    return 0;
  if ( a3 == 1 )
  {
    if ( !GetDlgItemTextA(hDlg, 2101, &PathName, 260)
      || (unsigned int)(&PathName + strlen(&PathName) + 1 - &byte_4091E5) < 3
      || byte_4091E5 != 58 && (PathName != 92 || byte_4091E5 != 92) )
    {
      MsgBox2Param(hDlg, 1215, 0, 0, 16, 0);
      return 1;
    }
    if ( GetFileAttributesA(&PathName) == -1 )
    {
      if ( MsgBox2Param(hDlg, 1354, &PathName, 0, 32, 4) != 6 )
        return 1;
      if ( !CreateDirectoryA(&PathName, 0) )
      {
        MsgBox2Param(hDlg, 1227, &PathName, 0, 16, 0);
        return 1;
      }
    }
    AddPath(&PathName, (STRSAFE_LPSTR)pszCabPath);
    if ( !IsGoodTempDir(&PathName) )
    {
      MsgBox2Param(hDlg, 1214, 0, 0, 16, 0);
      return 1;
    }
    if ( PathName == 92 && byte_4091E5 == 92 || IsEnoughSpace(&PathName, 1) )
      EndDialog(hDlg, 1);
    return 1;
  }
  if ( a3 == 2 )
  {
    EndDialog(hDlg, 0);
    g_dwExitCode = -2147023673;
    return 1;
  }
  if ( a3 != 2102 )
    return 1;
  if ( LoadStringA(g_hInst, 0x3E8u, Buffer, 512) )
  {
    if ( BrowseForDir(hDlg, v5, v5) && !SetDlgItemTextA(hDlg, 2101, &byte_4087A0) )
    {
      v6 = 1216;
      goto LABEL_10;
    }
    return 1;
  }
  v6 = 1201;
LABEL_10:
  MsgBox2Param(hDlg, v6, 0, 0, 16, 0);
  EndDialog(hDlg, 0);
  return 1;
}


int __stdcall OverwriteDlgProc(HWND hDlg, int a2, unsigned int nResult, int a4)
{
  HWND DesktopWindow; // eax

  switch ( a2 )
  {
    case 16:
      EndDialog(hDlg, 2);
      break;
    case 272:
      DesktopWindow = GetDesktopWindow();
      CenterWindow(hDlg, DesktopWindow);
      SetWindowTextA(hDlg, Destination);
      SetDlgItemTextA(hDlg, 2104, lpString);
      SetForegroundWindow(hDlg);
      break;
    case 273:
      if ( nResult >= 6 )
      {
        if ( nResult <= 7 )
        {
LABEL_9:
          EndDialog(hDlg, nResult);
          return 1;
        }
        if ( nResult == 2105 )
        {
          dword_4091DC = 1;
          goto LABEL_9;
        }
      }
      break;
    default:
      return 0;
  }
  return 1;
}


int __stdcall ExtractDlgProc(HWND hDlg, int a2, INT_PTR nResult, int a4)
{
  int v5; // eax
  HWND DesktopWindow; // eax
  HWND DlgItem; // eax
  HWND v8; // eax

  switch ( a2 )
  {
    case 16:
LABEL_18:
      dword_4091D8 = 1;
      goto LABEL_19;
    case 258:
      if ( nResult != 27 )
        return 1;
      goto LABEL_18;
    case 272:
      g_hwndExtractDlg = hDlg;
      DesktopWindow = GetDesktopWindow();
      CenterWindow(hDlg, DesktopWindow);
      if ( g_fOSSupportsFullUI )
      {
        DlgItem = GetDlgItem(hDlg, 2107);
        SendMessageA(DlgItem, 0x464u, 0, 3001);
        v8 = GetDlgItem(hDlg, 2107);
        SendMessageA(v8, 0x465u, 0xFFFFFFFF, -65536);
      }
      SetWindowTextA(hDlg, Destination);
      hThread = CreateThread(0, 0, ExtractThread, 0, 0, &ThreadId);
      if ( !hThread )
      {
        MsgBox2Param(hDlg, 1208, 0, 0, 16, 0);
        EndDialog(hDlg, 0);
      }
      return 1;
    case 273:
      if ( nResult != 2 )
        return 1;
      ResetEvent(g_hCancelEvent);
      v5 = MsgBox2Param(g_hwndExtractDlg, 1202, pszCabPath, 0, 32, 4);
      if ( v5 != 6 && v5 != 1 )
      {
        SetEvent(g_hCancelEvent);
        return 1;
      }
      dword_4091D8 = 1;
      SetEvent(g_hCancelEvent);
      WaitForObject(hThread);
LABEL_19:
      EndDialog(hDlg, 0);
      return 1;
  }
  if ( a2 != 4001 )
    return 0;
  TerminateThread(hThread, 0);
  EndDialog(hDlg, nResult);
  return 1;
}


DWORD __thiscall WaitForObject(void *this)
{
  int v1; // esi
  DWORD result; // eax
  tagMSG Msg; // [esp+8h] [ebp-20h] BYREF
  HANDLE pHandles; // [esp+24h] [ebp-4h] BYREF

  pHandles = this;
  v1 = 0;
  while ( 1 )
  {
    result = MsgWaitForMultipleObjects(1u, &pHandles, 0, 0xFFFFFFFF, 0x4FFu);
    if ( !result )
      break;
    if ( PeekMessageA(&Msg, 0, 0, 0, 1u) )
    {
      do
      {
        if ( Msg.message == 18 )
          v1 = 1;
        else
          DispatchMessageA(&Msg);
        result = PeekMessageA(&Msg, 0, 0, 0, 1u);
      }
      while ( result );
      if ( v1 )
        break;
    }
  }
  return result;
}


BOOL __thiscall CheckOSVersion(_DWORD *this)
{
  int v2; // edi
  int v3; // esi
  __int16 v4; // cx
  char *v5; // ebx
  unsigned int v6; // edx
  unsigned int v7; // ecx
  int v8; // eax
  bool v9; // cc
  int v10; // ebx
  char *v11; // ecx
  const CHAR *v12; // edi
  int v13; // ecx
  int v14; // eax
  int v15; // eax
  bool v16; // zf
  char *v18; // [esp+1Ch] [ebp-1B4h]
  int v19; // [esp+20h] [ebp-1B0h]
  int v21; // [esp+28h] [ebp-1A8h] BYREF
  int v22; // [esp+2Ch] [ebp-1A4h]
  CHAR *v23; // [esp+30h] [ebp-1A0h]
  _OSVERSIONINFOA VersionInformation; // [esp+34h] [ebp-19Ch] BYREF
  CHAR v25[260]; // [esp+C8h] [ebp-108h] BYREF

  VersionInformation.dwOSVersionInfoSize = 148;
  v2 = 0;
  v3 = 0;
  if ( !GetVersionExA(&VersionInformation) )
  {
    v3 = 1204;
LABEL_41:
    MsgBox2Param(0, v3, 0, 0, 16, 0);
    return v3 == 0;
  }
  v4 = 2;
  if ( VersionInformation.dwPlatformId == 1 )
  {
    v4 = 0;
    g_fOSSupportsFullUI = 1;
    g_fOSSupportsINFInstalls = 1;
    goto LABEL_13;
  }
  if ( VersionInformation.dwPlatformId != 2 )
  {
    v3 = 1226;
    goto LABEL_41;
  }
  g_wOSVer = 2;
  g_fOSSupportsFullUI = 1;
  g_fOSSupportsINFInstalls = 1;
  if ( VersionInformation.dwMajorVersion <= 3 )
  {
    v4 = 1;
    g_wOSVer = 1;
    if ( VersionInformation.dwMajorVersion < 3 || VersionInformation.dwMinorVersion < 0x33 )
    {
      g_fOSSupportsFullUI = 0;
      g_fOSSupportsINFInstalls = 0;
    }
    goto LABEL_14;
  }
  if ( VersionInformation.dwMajorVersion >= 5 )
  {
    v4 = 3;
LABEL_13:
    g_wOSVer = v4;
  }
LABEL_14:
  if ( dword_408A34 || !this )
    return v3 == 0;
  v21 = 0;
  v5 = (char *)this + (v4 != 0 ? 4 : 64);
  v23 = 0;
  v18 = v5;
  while ( 1 )
  {
    v22 = 24 * v2;
    v19 = CompareVersion(
            VersionInformation.dwMajorVersion,
            VersionInformation.dwMinorVersion,
            *(_DWORD *)&v5[24 * v2],
            *(_DWORD *)&v5[24 * v2 + 4]);
    v8 = CompareVersion(v7, v6, *(_DWORD *)&v5[v22 + 12], *(_DWORD *)&v5[v22 + 16]);
    if ( v19 >= 0 && v8 <= 0 )
    {
      if ( !v19 )
      {
        if ( v8 )
        {
          if ( (unsigned int)LOWORD(VersionInformation.dwBuildNumber) >= *(_DWORD *)&v5[v22 + 8] )
            goto LABEL_37;
        }
        else if ( (unsigned int)LOWORD(VersionInformation.dwBuildNumber) >= *(_DWORD *)&v5[v22 + 8] )
        {
          v9 = (unsigned int)LOWORD(VersionInformation.dwBuildNumber) <= *(_DWORD *)&v5[v22 + 20];
          goto LABEL_27;
        }
LABEL_28:
        if ( v2 )
        {
          v3 = 1356;
          goto LABEL_30;
        }
        goto LABEL_33;
      }
      if ( v8 )
        goto LABEL_37;
      v9 = (unsigned int)LOWORD(VersionInformation.dwBuildNumber) <= *(_DWORD *)&v5[v22 + 20];
LABEL_27:
      if ( v9 )
        goto LABEL_37;
      goto LABEL_28;
    }
    if ( v23 == (CHAR *)1 )
      break;
LABEL_33:
    v21 = ++v2;
    v23 = (CHAR *)v2;
    if ( v2 >= 2 )
      goto LABEL_36;
  }
  v3 = 1356;
LABEL_36:
  if ( v3 )
    goto LABEL_30;
LABEL_37:
  if ( !this[31] || CheckFileVersion((int)this, v25, (int)this, &v21) )
    return v3 == 0;
  v2 = v21;
  v3 = 1357;
LABEL_30:
  v23 = 0;
  v10 = 0;
  if ( v3 == 1357 )
  {
    v11 = (char *)&this[15 * v2 + 33] + this[32];
    v23 = v25;
  }
  else
  {
    v11 = v18;
  }
  if ( v11 )
  {
    v12 = (char *)this + *((_DWORD *)v11 + 13) + 132;
    if ( (*((_DWORD *)v11 + 12) & 1) != 0 )
      v10 = 260;
    else
      v10 = (*((_DWORD *)v11 + 12) & 2) != 0 ? 0x101 : 0;
  }
  else
  {
    v12 = 0;
  }
  if ( (word_408A38 & 1) == 0 && v12 && *v12 )
  {
    MessageBeep(0);
    if ( RunningOnWin95BiDiLoc() && IsBiDiLocalizedBinary(v13, v13) )
      v14 = 1572912;
    else
      v14 = 48;
    v15 = MessageBoxA(0, v12, Destination, v10 | v14);
    if ( (v10 & 4) != 0 )
    {
      v16 = v15 == 6;
    }
    else
    {
      if ( (v10 & 1) == 0 )
        return v3 == 0;
      v16 = v15 == 1;
    }
    if ( v16 )
      v3 = 0;
  }
  else
  {
    MsgBox2Param(0, v3, Destination, v23, 48, 0);
  }
  return v3 == 0;
}


int __stdcall DisplayLicense()
{
  rsize_t Resource; // esi
  CHAR *v1; // eax
  int v3; // esi

  Resource = GetResource("LICENSE", 0, 0);
  v1 = (CHAR *)LocalAlloc(0x40u, Resource + 1);
  g_szLicense = v1;
  if ( !v1 )
  {
    MsgBox2Param(0, 1205, 0, 0, 16, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  if ( !GetResource("LICENSE", v1, Resource) )
  {
    MsgBox2Param(0, 1201, 0, 0, 16, 0);
    LocalFree((HLOCAL)g_szLicense);
    g_dwExitCode = -2147023084;
    return 0;
  }
  if ( lstrcmpA(g_szLicense, "<None>") )
  {
    v3 = MyDialogBox(0, LicenseDlgProc, 0, 0);
    LocalFree((HLOCAL)g_szLicense);
    if ( !v3 )
    {
      g_dwExitCode = -2147023673;
      return 0;
    }
  }
  else
  {
    LocalFree((HLOCAL)g_szLicense);
  }
  g_dwExitCode = 0;
  return 1;
}


int __stdcall ExtractFiles()
{
  unsigned int i; // eax
  int Thread; // eax
  void *v3; // [esp+0h] [ebp-4h]

  for ( i = 0; i < 240; i += 6 )
    g_FileTable[i] = 1;
  if ( (word_408A38 & 1) != 0 || (dword_409A34 & 1) != 0 )
    Thread = ExtractThread(v3);
  else
    Thread = MyDialogBox(0, ExtractDlgProc, 0, 0);
  if ( !Thread )
  {
    g_dwExitCode = -2147023829;
    return 0;
  }
  if ( !TravelUpdatedFiles(ProcessUpdatedFile_Write) )
    return 0;
  g_dwExitCode = 0;
  return 1;
}


int __stdcall RunInstallCommand()
{
  int v0; // esi
  int v1; // edi
  unsigned int Resource; // eax
  unsigned int v3; // ebx
  char *v4; // ecx
  unsigned int v5; // eax
  WORD v6; // ax
  const CHAR *v7; // ecx
  size_t *v8; // ecx
  int v9; // esi
  HMODULE Library; // eax
  HMODULE v11; // ebx
  FARPROC DoInfInstall; // edx
  HLOCAL v13; // edi
  int v14; // eax
  const char *v16; // [esp+0h] [ebp-1A0h]
  size_t v17; // [esp+4h] [ebp-19Ch]
  HLOCAL hMem; // [esp+10h] [ebp-190h] BYREF
  int v19; // [esp+14h] [ebp-18Ch] BYREF
  int Destination; // [esp+18h] [ebp-188h] BYREF
  unsigned int v21; // [esp+1Ch] [ebp-184h]
  int v22; // [esp+20h] [ebp-180h]
  int v23; // [esp+24h] [ebp-17Ch]
  _DWORD v24[5]; // [esp+28h] [ebp-178h] BYREF
  __int16 v25; // [esp+3Ch] [ebp-164h]
  int v26; // [esp+40h] [ebp-160h]
  int v27; // [esp+44h] [ebp-15Ch]
  _STARTUPINFOA StartupInfo; // [esp+48h] [ebp-158h] BYREF
  CHAR String1[268]; // [esp+90h] [ebp-110h] BYREF

  v0 = 0;
  g_dwExitCode = 0;
  v1 = 0;
  v22 = 0;
  v23 = 0;
  if ( !dword_408A28 )
  {
    Resource = GetResource("REBOOT", &dword_409A2C, 4u);
    if ( !Resource || Resource > 4 )
    {
LABEL_26:
      MsgBox2Param(0, 1201, 0, 0, 16, 0);
      g_dwExitCode = -2147023084;
      return 0;
    }
  }
  v3 = 0;
  v21 = 0;
  while ( 1 )
  {
    v19 = 0;
    memset(&StartupInfo, 0, sizeof(StartupInfo));
    StartupInfo.cb = 68;
    if ( byte_408C42 )
    {
      StringCopyWorkerA(v4, (size_t)&byte_408C42, (size_t *)v4, v16, v17);
      goto LABEL_28;
    }
    v5 = GetResource("SHOWWINDOW", &Destination, 4u);
    if ( !v5 || v5 > 4 )
      goto LABEL_26;
    switch ( Destination )
    {
      case 1:
        StartupInfo.dwFlags = 1;
        v6 = 0;
LABEL_12:
        StartupInfo.wShowWindow = v6;
        break;
      case 2:
        StartupInfo.dwFlags = 1;
        v6 = 6;
        goto LABEL_12;
      case 3:
        StartupInfo.dwFlags = 1;
        StartupInfo.wShowWindow = 3;
        break;
    }
    if ( v3 )
      goto LABEL_28;
    if ( word_408A38 )
    {
      if ( (word_408A38 & 1) != 0 )
      {
        v7 = "ADMQCMD";
      }
      else
      {
        if ( (word_408A38 & 2) == 0 )
          return 0;
        v7 = "USRQCMD";
      }
      if ( !GetResource(v7, String1, 0x104u) )
        goto LABEL_26;
      if ( CompareStringA(0x7Fu, 1u, String1, -1, "<None>", -1) )
      {
        v0 = 1;
        v22 = 1;
      }
    }
    if ( !v0 )
      break;
LABEL_32:
    if ( !AnalyzeCmd(String1, (char **)&hMem, &v19) )
      return 0;
    v9 = v19;
    if ( !v1 && g_wOSVer != 1 && g_CMD )
    {
      if ( v19 )
        goto LABEL_39;
      v23 = 1;
      AddRegRunOnce();
    }
    if ( !v9 )
      goto LABEL_56;
LABEL_39:
    if ( !g_fOSSupportsINFInstalls )
    {
      MsgBox2Param(0, 1223, 0, 0, 16, 0);
      LocalFree(hMem);
      g_dwExitCode = -2147023829;
      return 0;
    }
    if ( !v9 || (dword_409A34 & 4) == 0 )
    {
LABEL_56:
      v13 = hMem;
      if ( !RunApps((LPSTR)hMem, &StartupInfo) )
        goto LABEL_60;
      goto LABEL_57;
    }
    Library = (HMODULE)MyLoadLibrary(v8);
    v11 = Library;
    if ( !Library )
    {
      MsgBox2Param(0, 1224, "advpack.dll", 0, 16, 0);
      goto LABEL_63;
    }
    DoInfInstall = GetProcAddress(Library, aDoinfinstall);
    v19 = (int)DoInfInstall;
    if ( !DoInfInstall )
    {
      MsgBox2Param(0, 1225, aDoinfinstall, 0, 16, 0);
      FreeLibrary(v11);
LABEL_63:
      LocalFree(hMem);
      g_dwExitCode = MyGetLastError();
      return 0;
    }
    v13 = hMem;
    v24[0] = 0;
    v24[4] = String1;
    v25 = g_wOSVer;
    v14 = (unsigned __int16)word_408A38;
    v24[1] = ::Destination;
    v24[2] = hMem;
    v24[3] = &PathName;
    v26 = (unsigned __int16)word_408A38;
    if ( dword_408A30 )
    {
      v14 = (unsigned __int16)word_408A38 | 0x10000;
      v26 = v14;
    }
    if ( (dword_409A34 & 8) != 0 )
    {
      v14 |= 0x20000u;
      v26 = v14;
    }
    if ( (dword_409A34 & 0x10) != 0 )
    {
      v14 |= 0x40000u;
      v26 = v14;
    }
    if ( (dword_408D48 & 0x40) != 0 )
    {
      v14 |= 0x80000u;
      v26 = v14;
    }
    if ( (dword_408D48 & 0x80u) != 0 )
      v26 = v14 | 0x100000;
    v27 = dword_409A38;
    g_dwExitCode = ((int (__thiscall *)(FARPROC, _DWORD *))v19)(DoInfInstall, v24);
    if ( g_dwExitCode < 0 )
    {
      FreeLibrary(v11);
LABEL_60:
      LocalFree(v13);
      return 0;
    }
    FreeLibrary(v11);
    v3 = v21;
LABEL_57:
    LocalFree(v13);
    v21 = ++v3;
    if ( v3 >= 2 )
      goto LABEL_66;
    v0 = v22;
    v1 = v23;
  }
  if ( !GetResource("RUNPROGRAM", String1, 0x104u) )
    goto LABEL_26;
LABEL_28:
  if ( v3 != 1 )
    goto LABEL_32;
  if ( !GetResource("POSTRUNPROGRAM", String1, 0x104u) )
    goto LABEL_26;
  if ( !byte_408C42 && CompareStringA(0x7Fu, 1u, String1, -1, "<None>", -1) != 2 )
    goto LABEL_32;
LABEL_66:
  if ( g_bConvertRunOnce )
    ConvertRegRunOnce();
  return 1;
}


int __fastcall RunApps(LPSTR lpCommandLine, LPSTARTUPINFOA lpStartupInfo)
{
  int v3; // esi
  int result; // eax
  DWORD LastError; // eax
  _PROCESS_INFORMATION ProcessInformation; // [esp+Ch] [ebp-21Ch] BYREF
  DWORD ExitCode; // [esp+1Ch] [ebp-20Ch] BYREF
  CHAR Buffer[516]; // [esp+20h] [ebp-208h] BYREF

  v3 = 1;
  result = 0;
  if ( lpCommandLine )
  {
    memset(&ProcessInformation, 0, sizeof(ProcessInformation));
    if ( CreateProcessA(0, lpCommandLine, 0, 0, 0, 0x20u, 0, 0, lpStartupInfo, &ProcessInformation) )
    {
      WaitForSingleObject(ProcessInformation.hProcess, 0xFFFFFFFF);
      GetExitCodeProcess(ProcessInformation.hProcess, &ExitCode);
      if ( !dword_408A28 && (dword_409A2C & 1) != 0 && (dword_409A2C & 2) == 0 && (ExitCode & 0xFF000000) == 0xAA000000 )
        dword_409A2C = ExitCode;
      savAppExitCode(ExitCode);
      CloseHandle(ProcessInformation.hThread);
      CloseHandle(ProcessInformation.hProcess);
      if ( (dword_409A34 & 0x400) == 0 || (ExitCode & 0x80000000) == 0 )
        return v3;
    }
    else
    {
      g_dwExitCode = MyGetLastError();
      LastError = GetLastError();
      FormatMessageA(0x1000u, 0, LastError, 0, Buffer, 0x200u, 0);
      MsgBox2Param(0, 1220, lpCommandLine, Buffer, 16, 0);
    }
    return 0;
  }
  return result;
}


void __fastcall savAppExitCode(int a1)
{
  if ( (dword_409A34 & 0x800) != 0 )
    goto LABEL_2;
  if ( CheckReboot() == 2 || (a1 & 0xFF000000) == 0xAA000000 && (a1 & 1) != 0 )
  {
    g_dwExitCode = 3010;
  }
  else if ( (dword_409A34 & 0x200) != 0 )
  {
LABEL_2:
    g_dwExitCode = a1;
  }
}


HLOCAL __stdcall FinishMessage()
{
  rsize_t Resource; // edi
  CHAR *v1; // eax
  CHAR *v2; // esi

  Resource = GetResource("FINISHMSG", 0, 0);
  v1 = (CHAR *)LocalAlloc(0x40u, 4 * Resource + 4);
  v2 = v1;
  if ( !v1 )
    return (HLOCAL)MsgBox2Param(0, 1205, 0, 0, 16, 0);
  if ( GetResource("FINISHMSG", v1, Resource) )
  {
    if ( lstrcmpA(v2, "<None>") )
      MsgBox2Param(0, 1001, v2, 0, 64, 0);
  }
  else
  {
    MsgBox2Param(0, 1201, 0, 0, 16, 0);
  }
  return LocalFree(v2);
}


int __stdcall BrowseCallback(HWND hWnd, int a2, int a3, LPARAM lParam)
{
  if ( a2 == 1 )
    SendMessageA(hWnd, 0x466u, 1u, lParam);
  return 0;
}


BOOL __thiscall BrowseForDir(void *this, int a2, int a3)
{
  HMODULE LibraryA; // eax
  HMODULE v5; // edi
  LPSTR v6; // eax
  int v7; // eax
  int v9; // edx
  size_t v10; // [esp+0h] [ebp-3Ch]
  const char *v11; // [esp+4h] [ebp-38h]
  _DWORD v12[8]; // [esp+Ch] [ebp-30h] BYREF
  FARPROC ProcAddress; // [esp+2Ch] [ebp-10h]
  FARPROC SHGetPathFromIDList; // [esp+30h] [ebp-Ch]
  FARPROC SHBrowseForFolder; // [esp+34h] [ebp-8h]
  LPSTR v16; // [esp+38h] [ebp-4h]

  LibraryA = LoadLibraryA(aShell32Dll);
  v5 = LibraryA;
  if ( !LibraryA )
  {
    v9 = 1218;
    goto LABEL_16;
  }
  SHBrowseForFolder = GetProcAddress(LibraryA, aShbrowseforfol);
  if ( !SHBrowseForFolder
    || (ProcAddress = GetProcAddress(v5, (LPCSTR)0xC3)) == 0
    || (SHGetPathFromIDList = GetProcAddress(v5, aShgetpathfromi)) == 0 )
  {
    FreeLibrary(v5);
    v9 = 1217;
LABEL_16:
    MsgBox2Param(this, v9, 0, 0, 16, 0);
    return 0;
  }
  if ( !g_szBrowsePath[0] )
  {
    GetTempPathA(0x104u, g_szBrowsePath);
    v6 = CharPrevA(g_szBrowsePath, &g_szBrowsePath[strlen(g_szBrowsePath)]);
    v16 = v6;
    if ( *v6 == 92 && *CharPrevA(g_szBrowsePath, v6) != 58 )
      *v16 = 0;
  }
  byte_4087A0 = 0;
  v12[0] = this;
  v12[1] = 0;
  v12[2] = 0;
  v12[3] = Buffer;
  v12[4] = 1;
  v12[5] = BrowseCallback;
  v12[6] = g_szBrowsePath;
  v7 = ((int (__thiscall *)(FARPROC, _DWORD *))SHBrowseForFolder)(SHBrowseForFolder, v12);
  SHBrowseForFolder = (FARPROC)v7;
  if ( v7 )
  {
    ((void (__thiscall *)(FARPROC, int, CHAR *))SHGetPathFromIDList)(SHGetPathFromIDList, v7, g_szBrowsePath);
    if ( g_szBrowsePath[0] )
      StringCchCopyA(g_szBrowsePath, v10, v11);
    ((void (__thiscall *)(FARPROC, FARPROC))ProcAddress)(ProcAddress, SHBrowseForFolder);
  }
  FreeLibrary(v5);
  return byte_4087A0 != 0;
}


BOOL __fastcall CenterWindow(HWND hWnd, HWND a2)
{
  int v3; // ebx
  int v4; // edi
  HDC DC; // esi
  int v6; // esi
  int v7; // ecx
  int v9; // [esp+Ch] [ebp-38h]
  int v10; // [esp+10h] [ebp-34h]
  int DeviceCaps; // [esp+14h] [ebp-30h]
  int v12; // [esp+18h] [ebp-2Ch]
  tagRECT Rect; // [esp+20h] [ebp-24h] BYREF
  struct tagRECT v15; // [esp+30h] [ebp-14h] BYREF

  GetWindowRect(hWnd, &Rect);
  v3 = Rect.bottom - Rect.top;
  v12 = Rect.right - Rect.left;
  GetWindowRect(a2, &v15);
  v4 = v15.right - v15.left;
  v10 = v15.bottom - v15.top;
  DC = GetDC(hWnd);
  DeviceCaps = GetDeviceCaps(DC, 8);
  v9 = GetDeviceCaps(DC, 10);
  ReleaseDC(hWnd, DC);
  v6 = v15.left + (v4 - v12) / 2;
  if ( v6 >= 0 )
  {
    if ( v6 + v12 > DeviceCaps )
      v6 = DeviceCaps - v12;
  }
  else
  {
    v6 = 0;
  }
  v7 = v15.top + (v10 - v3) / 2;
  if ( v7 >= 0 )
  {
    if ( v7 + v3 > v9 )
      v7 = v9 - v3;
  }
  else
  {
    v7 = 0;
  }
  return SetWindowPos(hWnd, 0, v6, v7, 0, 0, 5u);
}


int __fastcall MsgBox2Param(HWND a1, UINT a2, const char *a3, const char *a4, UINT uType, int a6)
{
  int v6; // ecx
  bool v7; // zf
  UINT v8; // eax
  unsigned int v10; // kr00_4
  SIZE_T v11; // esi
  char *v12; // edi
  unsigned int v13; // kr04_4
  int v14; // ecx
  int v15; // eax
  int v16; // esi
  size_t v17; // [esp+0h] [ebp-250h]
  const char *v18; // [esp+4h] [ebp-24Ch]
  CHAR Buffer[512]; // [esp+14h] [ebp-23Ch] BYREF
  CHAR Text[56]; // [esp+214h] [ebp-3Ch] BYREF

  strcpy(Text, "LoadString() Error.  Could not load string resource.");
  if ( (word_408A38 & 1) != 0 )
    return 1;
  Buffer[0] = 0;
  LoadStringA(g_hInst, a2, Buffer, 512);
  if ( !Buffer[0] )
  {
    if ( !RunningOnWin95BiDiLoc() || (v7 = IsBiDiLocalizedBinary(v6, v6) == 0, v8 = 1638416, v7) )
      v8 = 65552;
    MessageBoxA(a1, Text, Destination, v8);
    return -1;
  }
  v10 = strlen(Buffer);
  if ( a4 )
  {
    v11 = strlen(a4) + strlen(a3) + v10 + 100;
    v12 = (char *)LocalAlloc(0x40u, v11);
    if ( v12 )
    {
      StringCchPrintfA(v12, v11, Buffer, a3, a4);
      goto LABEL_16;
    }
    return -1;
  }
  if ( a3 )
  {
    v13 = strlen(a3);
    v12 = (char *)LocalAlloc(0x40u, v10 + v13 + 100);
    if ( !v12 )
      return -1;
    StringCchPrintfA(v12, v10 + v13 + 100, Buffer, a3);
  }
  else
  {
    v12 = (char *)LocalAlloc(0x40u, v10 + 1);
    if ( !v12 )
      return -1;
    StringCchCopyA(Buffer, v17, v18);
  }
LABEL_16:
  MessageBeep(uType);
  if ( !RunningOnWin95BiDiLoc() || (v7 = IsBiDiLocalizedBinary(v14, v14) == 0, v15 = 1638400, v7) )
    v15 = 0x10000;
  v16 = MessageBoxA(a1, v12, Destination, a6 | uType | v15);
  LocalFree(v12);
  return v16;
}


DWORD __fastcall GetResource(LPCSTR lpName, void *Destination, rsize_t DestinationSize)
{
  HRSRC ResourceA; // eax
  DWORD result; // eax
  rsize_t v7; // esi
  HRSRC v8; // eax
  HGLOBAL Resource; // eax
  const void *v10; // eax
  void *v11; // edi

  ResourceA = FindResourceA(0, lpName, (LPCSTR)0xA);
  result = SizeofResource(0, ResourceA);
  v7 = result;
  if ( result <= DestinationSize && Destination )
  {
    if ( result
      && (v8 = FindResourceA(0, lpName, (LPCSTR)0xA),
          Resource = LoadResource(0, v8),
          v10 = LockResource(Resource),
          (v11 = (void *)v10) != 0) )
    {
      _memcpy_s(Destination, DestinationSize, v10, v7);
      FreeResource(v11);
      return v7;
    }
    else
    {
      return 0;
    }
  }
  return result;
}


int __fastcall CatDirAndFile(const char *a1, char *a2, char *pszDest)
{
  size_t v5; // [esp+0h] [ebp-8h]
  size_t v6; // [esp+0h] [ebp-8h]
  const char *v7; // [esp+4h] [ebp-4h]
  const char *v8; // [esp+4h] [ebp-4h]

  StringCchCopyA(a2, v5, v7);
  if ( a1[strlen(a1) - 1] != 92 && a1[strlen(a1) - 1] != 47 && StringCchCatA((STRSAFE_LPSTR)"\\", v6, v8) < 0 )
    return 0;
  StringCchCatA(pszDest, v6, v8);
  return 1;
}


int __thiscall CheckOverwrite(LPCSTR lpFileName)
{
  int v3; // edi
  int v4; // eax
  int v5; // eax

  if ( !FileExists(lpFileName) )
    return 1;
  if ( dword_4091DC )
    goto LABEL_9;
  if ( (word_408A38 & 1) != 0 )
    goto LABEL_9;
  v3 = 0;
  lpString = lpFileName;
  v4 = MyDialogBox(g_hwndExtractDlg, OverwriteDlgProc, 0, 6) - 6;
  if ( !v4 )
    goto LABEL_9;
  v5 = v4 - 1;
  if ( v5 )
  {
    if ( v5 == 2098 )
      dword_4091DC = 1;
LABEL_9:
    SetFileAttributesA(lpFileName, 0x80u);
    return 1;
  }
  return v3;
}


int __usercall AddFile@<eax>(STRSAFE_LPSTR pszDest@<ecx>, size_t a2@<ebx>)
{
  _DWORD *v3; // esi
  HLOCAL v5; // eax
  const char *v6; // [esp+0h] [ebp-8h]

  v3 = LocalAlloc(0x40u, 8u);
  if ( !v3 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4B5u, 0, 0, 0x10u, 0);
    return 0;
  }
  v5 = LocalAlloc(0x40u, strlen(pszDest) + 1);
  *v3 = v5;
  if ( !v5 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4B5u, 0, 0, 0x10u, 0);
    LocalFree(v3);
    return 0;
  }
  strlen(pszDest);
  StringCchCopyA(pszDest, a2, v6);
  v3[1] = hMem;
  hMem = v3;
  return 1;
}


HANDLE __fastcall Win32Open(LPCSTR lpPathName, __int16 a2)
{
  DWORD v3; // edi
  DWORD v4; // esi
  HANDLE result; // eax

  v3 = (a2 & 3) != 0 ? 0x40000000 : 0x80000000;
  if ( (a2 & 0x100) != 0 )
  {
    if ( (a2 & 0x400) != 0 )
      v4 = 1;
    else
      v4 = (a2 & 0x200) != 0 ? 2 : 4;
  }
  else
  {
    v4 = (a2 & 0x200) != 0 ? 5 : 3;
  }
  result = CreateFileA(lpPathName, (a2 & 3) != 0 ? 0x40000000 : 0x80000000, 0, 0, v4, 0x80u, 0);
  if ( result == (HANDLE)-1 && v4 != 3 )
  {
    MakeDirectory(lpPathName);
    return CreateFileA(lpPathName, v3, 0, 0, v4, 0x80u, 0);
  }
  return result;
}


void __thiscall MakeDirectory(CHAR *lpPathName)
{
  CHAR v2; // cl
  CHAR v3; // al
  int v4; // ebx
  LPSTR v5; // esi

  v2 = *lpPathName;
  if ( v2 )
  {
    v3 = lpPathName[1];
    v4 = 0;
    v5 = lpPathName + 2;
    if ( v3 == 58 && *v5 == 92 )
    {
      v5 = lpPathName + 3;
    }
    else
    {
      if ( v2 != 92 || v3 != 92 )
      {
        v5 = lpPathName + 1;
        goto LABEL_16;
      }
      v4 = 2;
    }
    while ( 1 )
    {
      v3 = *v5;
LABEL_16:
      if ( !v3 )
        break;
      if ( v3 == 92 && *(v5 - 1) != 58 )
      {
        if ( v4 )
        {
          --v4;
        }
        else
        {
          *v5 = 0;
          CreateDirectoryA(lpPathName, 0);
          *v5 = 92;
        }
      }
      v5 = CharNextA(v5);
    }
  }
}


INT_PTR __cdecl openfunc(const CHAR *pszFile, __int16 oflag)
{
  int *v2; // eax
  int v3; // esi
  int v5; // ecx
  int v6; // eax
  int v7; // ecx

  v2 = g_FileTable;
  v3 = 0;
  do
  {
    if ( *v2 == 1 )
      break;
    v2 += 6;
    ++v3;
  }
  while ( (int)v2 < (int)&g_uInfRebootOn );
  if ( v3 == 40 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4BBu, 0, 0, 0x10u, 0);
    return -1;
  }
  if ( lstrcmpA(pszFile, pszCabinet) )
  {
    if ( (oflag & 8) != 0 )
      v7 = -1;
    else
      v7 = (int)Win32Open(pszFile, oflag);
    dword_408D74[6 * v3] = v7;
    if ( v7 == -1 )
    {
      return -1;
    }
    else
    {
      g_FileTable[6 * v3] = 0;
      dword_408D64[6 * v3] = 0;
    }
  }
  else
  {
    if ( (oflag & 0x10B) != 0 )
      return -1;
    v5 = 6 * v3;
    dword_408D68[v5] = (int)g_Sess;
    v6 = dword_409144;
    g_FileTable[v5] = 0;
    dword_408D64[v5] = 1;
    dword_408D70[v5] = v6;
    dword_408D6C[v5] = 0;
  }
  return v3;
}


UINT __cdecl readfunc(INT_PTR hf, void *pv, UINT cb)
{
  int v3; // eax
  int v4; // ecx
  size_t v5; // esi

  v3 = dword_408D64[6 * hf];
  if ( !v3 )
  {
    if ( ReadFile((HANDLE)dword_408D74[6 * hf], pv, cb, &cb, 0) )
      return cb;
    return -1;
  }
  if ( v3 != 1 )
    return -1;
  v4 = dword_408D6C[6 * hf];
  v5 = cb;
  if ( cb >= dword_408D70[6 * hf] - v4 )
    v5 = dword_408D70[6 * hf] - v4;
  memcpy(pv, (const void *)(v4 + dword_408D68[6 * hf]), v5);
  dword_408D6C[6 * hf] += v5;
  return v5;
}


UINT __cdecl writefunc(INT_PTR hf, LPCVOID pv, UINT cb)
{
  UINT v4; // esi
  UINT v5; // eax

  WaitForObject(g_hCancelEvent);
  if ( dword_4091D8 )
    return -1;
  if ( !WriteFile((HANDLE)dword_408D74[6 * hf], pv, cb, &cb, 0) )
    return -1;
  v4 = cb;
  if ( cb != -1 )
  {
    v5 = cb + dword_409400;
    dword_409400 += cb;
    if ( g_fOSSupportsFullUI )
    {
      if ( g_hwndExtractDlg )
        SendDlgItemMessageA(g_hwndExtractDlg, 2106, 0x402u, 100 * v5 / dword_4093F8, 0);
    }
  }
  return v4;
}


int __cdecl closefunc(INT_PTR hf)
{
  int result; // eax

  if ( dword_408D64[6 * hf] == 1 )
  {
    result = 0;
    g_FileTable[6 * hf] = 1;
    dword_408D68[6 * hf] = 0;
    dword_408D70[6 * hf] = 0;
    dword_408D6C[6 * hf] = 0;
  }
  else if ( CloseHandle((HANDLE)dword_408D74[6 * hf]) )
  {
    result = 0;
    g_FileTable[6 * hf] = 1;
  }
  else
  {
    return -1;
  }
  return result;
}


DWORD __cdecl seekfunc(INT_PTR hf, LONG dist, int seektype)
{
  DWORD v3; // ecx
  DWORD result; // eax

  v3 = 1;
  if ( dword_408D64[6 * hf] == 1 )
  {
    switch ( seektype )
    {
      case 0:
        result = dist;
        goto LABEL_8;
      case 1:
        result = dword_408D6C[6 * hf] + dist;
        goto LABEL_8;
      case 2:
        result = dword_408D70[6 * hf] + dist;
LABEL_8:
        dword_408D6C[6 * hf] = result;
        return result;
    }
    return -1;
  }
  switch ( seektype )
  {
    case 0:
      v3 = 0;
LABEL_14:
      result = SetFilePointer((HANDLE)dword_408D74[6 * hf], dist, 0, v3);
      if ( result != -1 )
        return result;
      return -1;
    case 1:
      goto LABEL_14;
    case 2:
      v3 = 2;
      goto LABEL_14;
  }
  return -1;
}


BOOL __fastcall AdjustFileTime(int a1, WORD a2, WORD wFatTime)
{
  int v3; // esi
  struct _FILETIME FileTime; // [esp+4h] [ebp-10h] BYREF
  FILETIME CreationTime; // [esp+Ch] [ebp-8h] BYREF

  v3 = 6 * a1;
  return dword_408D64[6 * a1] != 1
      && DosDateTimeToFileTime(a2, wFatTime, &FileTime)
      && LocalFileTimeToFileTime(&FileTime, &CreationTime)
      && SetFileTime((HANDLE)dword_408D74[v3], &CreationTime, &CreationTime, &CreationTime);
}


HGLOBAL __cdecl allocfunc(ULONG cb)
{
  return GlobalAlloc(0, cb);
}


void __cdecl freefunc(HGLOBAL pv)
{
  GlobalFree(pv);
}


INT_PTR __cdecl fdiNotifyExtract(FDINOTIFICATIONTYPE fdint, PFDINOTIFICATION pfdin)
{
  USHORT attribs; // ax
  DWORD v4; // eax
  INT_PTR v5; // esi
  CHAR FileName[260]; // [esp+Ch] [ebp-108h] BYREF

  if ( dword_4091D8 )
  {
    if ( fdint == fdintCLOSE_FILE_INFO )
      closefunc(pfdin->hf);
    return -1;
  }
  switch ( fdint )
  {
    case fdintCABINET_INFO:
      return UpdateCabinetInfo(pfdin);
    case fdintPARTIAL_FILE:
      return 0;
    case fdintCOPY_FILE:
      if ( g_hwndExtractDlg )
        SetDlgItemTextA(g_hwndExtractDlg, 2103, pfdin->psz1);
      if ( (int)(strlen(pfdin->psz1) + strlen(&PathName) + 1) >= 260 || !CatDirAndFile(FileName, &PathName, pfdin->psz1) )
        return -1;
      if ( CheckOverwrite(FileName) )
      {
        v5 = openfunc(FileName, 33538);
        if ( v5 == -1 || !AddFile(FileName, (size_t)&PathName) )
          return -1;
        ++dword_4093F4;
        return v5;
      }
      return 0;
  }
  if ( fdint != fdintCLOSE_FILE_INFO )
  {
    if ( fdint == fdintNEXT_CABINET )
      return -1;
    return 0;
  }
  if ( (int)(strlen(pfdin->psz1) + strlen(&PathName) + 1) >= 260
    || !CatDirAndFile(FileName, &PathName, pfdin->psz1)
    || !AdjustFileTime(pfdin->hf, pfdin->date, pfdin->time) )
  {
    return -1;
  }
  closefunc(pfdin->hf);
  attribs = pfdin->attribs;
  v4 = attribs ? attribs & 0x27 : 128;
  if ( !SetFileAttributesA(FileName, v4) )
    return -1;
  return 1;
}


int __thiscall UpdateCabinetInfo(int this)
{
  size_t v3; // [esp+0h] [ebp-Ch]
  size_t v4; // [esp+0h] [ebp-Ch]
  size_t v5; // [esp+0h] [ebp-Ch]
  const char *v6; // [esp+4h] [ebp-8h]
  STRSAFE_LPCSTR v7; // [esp+4h] [ebp-8h]
  STRSAFE_LPCSTR v8; // [esp+4h] [ebp-8h]

  qmemcpy(&unk_40940C, &unk_40971C, 0x310u);
  StringCchCopyA(*(STRSAFE_LPSTR *)(this + 12), v3, v6);
  StringCchCopyA(*(STRSAFE_LPSTR *)(this + 4), v4, v7);
  StringCchCopyA(*(STRSAFE_LPSTR *)(this + 8), v5, v8);
  word_409A28 = *(_WORD *)(this + 30);
  word_409A2A = *(_WORD *)(this + 32);
  return 0;
}


BOOL VerifyCabinet()
{
  HFDI v0; // edi
  INT_PTR v1; // esi
  BOOL result; // eax
  ERF perf; // [esp+8h] [ebp-28h] BYREF
  FDICABINETINFO pfdici; // [esp+14h] [ebp-1Ch] BYREF

  memset(&pfdici, 0, sizeof(pfdici));
  v0 = _FDICreate(
         allocfunc,
         freefunc,
         (PFNOPEN)openfunc,
         readfunc,
         (PFNWRITE)writefunc,
         closefunc,
         (PFNSEEK)seekfunc,
         1,
         &perf);
  result = 0;
  if ( v0 )
  {
    v1 = openfunc(pszCabinet, 0x8000);
    if ( v1 != -1
      && _FDIIsCabinet(v0, v1, &pfdici)
      && pfdici.cbCabinet == dword_409144
      && !pfdici.hasprev
      && !pfdici.hasnext
      && closefunc(v1) != -1
      && _FDIDestroy(v0) )
    {
      return 1;
    }
  }
  return result;
}


DWORD __stdcall ExtractThread()
{
  HRSRC ResourceA; // eax
  HGLOBAL Resource; // eax
  DWORD result; // eax
  HWND DlgItem; // eax
  HWND v4; // eax
  BOOL v5; // esi
  HFDI v6; // eax
  void *v7; // edi

  dword_409144 = GetResource("CABINET", 0, 0);
  ResourceA = FindResourceA(0, "CABINET", (LPCSTR)0xA);
  Resource = LoadResource(0, ResourceA);
  result = (DWORD)LockResource(Resource);
  g_Sess = (HGLOBAL)result;
  if ( result )
  {
    if ( g_hwndExtractDlg )
    {
      DlgItem = GetDlgItem(g_hwndExtractDlg, 2114);
      ShowWindow(DlgItem, 0);
      v4 = GetDlgItem(g_hwndExtractDlg, 2113);
      ShowWindow(v4, 5);
    }
    if ( VerifyCabinet() )
    {
      v6 = _FDICreate(
             allocfunc,
             freefunc,
             (PFNOPEN)openfunc,
             readfunc,
             (PFNWRITE)writefunc,
             closefunc,
             (PFNSEEK)seekfunc,
             1,
             &perf);
      v7 = v6;
      if ( !v6
        || (v5 = _FDICopy(v6, pszCabinet, (LPSTR)pszCabPath, 0, fdiNotifyExtract, 0, &g_Sess)) && !_FDIDestroy(v7) )
      {
        MsgBox2Param(g_hwndExtractDlg, perf.erfOper + 1300, 0, 0, 0x10u, 0);
        v5 = 0;
      }
    }
    else
    {
      MsgBox2Param(g_hwndExtractDlg, 0x4BAu, 0, 0, 0x10u, 0);
      v5 = 0;
    }
    if ( g_Sess )
    {
      FreeResource(g_Sess);
      g_Sess = 0;
    }
    if ( !v5 && !dword_4091D8 )
      MsgBox2Param(0, 0x4F8u, 0, 0, 0x10u, 0);
    if ( (word_408A38 & 1) == 0 && (dword_409A34 & 1) == 0 )
      SendMessageA(g_hwndExtractDlg, 0xFA1u, v5, 0);
    return v5;
  }
  return result;
}


int __stdcall GetFileList()
{
  UINT v0; // edx

  if ( GetResource("FILESIZES", &g_dwFileSizes, 0x24u) != 36 )
  {
    v0 = 1201;
LABEL_3:
    MsgBox2Param(0, v0, 0, 0, 0x10u, 0);
    g_dwExitCode = -2147023084;
    return 0;
  }
  dword_4093F8 = dword_408A00;
  if ( !dword_408A00 )
  {
    v0 = 1222;
    goto LABEL_3;
  }
  GetResource("PACKINSTSPACE", &dword_409A38, 4u);
  if ( !TravelUpdatedFiles(ProcessUpdatedFile_Size) )
  {
    MsgBox2Param(0, 0x4C6u, 0, 0, 0x10u, 0);
    return 0;
  }
  return 1;
}


int __stdcall GetUsersPermission()
{
  rsize_t Resource; // esi
  char *v1; // eax
  char *v2; // edi
  int v4; // esi

  Resource = GetResource("UPROMPT", 0, 0);
  v1 = (char *)LocalAlloc(0x40u, Resource + 1);
  v2 = v1;
  if ( v1 )
  {
    if ( GetResource("UPROMPT", v1, Resource) )
    {
      if ( lstrcmpA(v2, "<None>") )
      {
        v4 = MsgBox2Param(0, 0x3E9u, v2, 0, 0x20u, 4);
        LocalFree(v2);
        if ( v4 != 6 )
        {
          g_dwExitCode = -2147023673;
          return 0;
        }
        g_dwExitCode = 0;
      }
      else
      {
        LocalFree(v2);
      }
      return 1;
    }
    MsgBox2Param(0, 0x4B1u, 0, 0, 0x10u, 0);
    LocalFree(v2);
    g_dwExitCode = -2147023084;
  }
  else
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
  }
  return 0;
}


void __thiscall DeleteExtractedFiles(char *this)
{
  LPCSTR *v1; // esi
  LPCSTR *v2; // edi
  int v3; // eax
  CHAR *v4; // [esp-8h] [ebp-114h]
  STRSAFE_PCNZCH szStart[65]; // [esp+4h] [ebp-108h] BYREF

  v1 = (LPCSTR *)hMem;
  if ( hMem )
  {
    do
    {
      v2 = v1;
      if ( !dword_408A24 && !dword_409A30 )
      {
        SetFileAttributesA(*v1, 0x80u);
        DeleteFileA(*v1);
      }
      v4 = (CHAR *)*v1;
      v1 = (LPCSTR *)v1[1];
      LocalFree(v4);
      LocalFree(v2);
    }
    while ( v1 );
  }
  v3 = g_CMD;
  if ( g_CMD && !dword_408A24 && !dword_409A30 )
  {
    StringCopyWorkerA(this, (size_t)&PathName, (size_t *)this, szStart[0], (size_t)szStart[1]);
    if ( (dword_409A34 & 0x20) != 0 )
      GetParentDir((LPCSTR)szStart);
    SetCurrentDirectoryA("..");
    DeleteMyDir((char *)szStart);
    v3 = g_CMD;
  }
  if ( g_wOSVer != 1 && v3 )
    CleanRegRunOnce((HKEY)this);
  g_CMD = 0;
}


int __fastcall GetNewTempDir(char *lpPathName, CHAR *lpszStart, int a3)
{
  int v5; // edi
  int v6; // edi
  size_t v8; // [esp+0h] [ebp-114h]
  const char *v9; // [esp+4h] [ebp-110h]
  char pszDest[260]; // [esp+Ch] [ebp-108h] BYREF

  v5 = 0;
  while ( 1 )
  {
    StringCchPrintfA(pszDest, 0x104u, "IXP%03d.TMP", v5++);
    StringCchCopyA(lpPathName, v8, v9);
    AddPath(lpszStart, pszDest);
    RemoveDirectoryA(lpszStart);
    if ( GetFileAttributesA(lpszStart) == -1 )
      break;
    if ( v5 >= 400 )
      goto LABEL_4;
  }
  if ( CreateDirectoryA(lpszStart, 0) )
  {
    v6 = 1;
    g_CMD = 1;
    return v6;
  }
LABEL_4:
  v6 = 0;
  if ( GetTempFileNameA(lpPathName, "IXP", 0, lpszStart) )
  {
    v6 = 1;
    DeleteFileA(lpszStart);
    CreateDirectoryA(lpszStart, 0);
  }
  return v6;
}


int __fastcall CreateAndValidateSubdir(char *a1, int a2, int a3)
{
  char *v3; // ecx
  const char *v5; // [esp+0h] [ebp-138h]
  const char *v6; // [esp+4h] [ebp-134h]
  _SYSTEM_INFO SystemInfo; // [esp+Ch] [ebp-12Ch] BYREF
  CHAR cchDest[260]; // [esp+30h] [ebp-108h] BYREF

  if ( a2 )
  {
    if ( !GetNewTempDir(a1, cchDest, (int)a1) )
      return 0;
    StringCopyWorkerA(v3, (size_t)cchDest, (size_t *)v3, v5, (size_t)v6);
    if ( (dword_409A34 & 0x20) != 0 )
    {
      GetSystemInfo(&SystemInfo);
      if ( SystemInfo.wProcessorArchitecture )
      {
        switch ( SystemInfo.wProcessorArchitecture )
        {
          case 1u:
            AddPath(&PathName, "mips");
            break;
          case 2u:
            AddPath(&PathName, "alpha");
            break;
          case 3u:
            AddPath(&PathName, "ppc");
            break;
        }
      }
      else
      {
        AddPath(&PathName, (STRSAFE_LPSTR)"i386");
      }
    }
    AddPath(&PathName, (STRSAFE_LPSTR)pszCabPath);
  }
  else
  {
    StringCchCopyA(a1, (size_t)v5, v6);
  }
  if ( !IsGoodTempDir(&PathName) )
  {
    if ( CreateDirectoryA(&PathName, 0) )
    {
      g_CMD = 1;
      goto LABEL_17;
    }
    g_dwExitCode = MyGetLastError();
    return 0;
  }
LABEL_17:
  if ( a3 && !IsEnoughSpace(&PathName, 0) )
  {
    if ( g_CMD )
    {
      g_CMD = 0;
      RemoveDirectoryA(&PathName);
    }
    return 0;
  }
  g_dwExitCode = 0;
  return 1;
}


BOOL __stdcall GetTempDirectory()
{
  rsize_t Resource; // edi
  HLOCAL v1; // eax
  void *v2; // esi
  int v4; // eax
  char *v5; // ecx
  UINT DriveTypeA; // eax
  UINT v7; // esi
  CHAR v8; // al
  char v9; // al
  DWORD FileAttributesA; // eax
  DWORD DirectoryA; // eax
  STRSAFE_LPSTR v12; // ecx
  const char *v13; // [esp+0h] [ebp-114h]
  size_t v14; // [esp+4h] [ebp-110h]
  CHAR RootPathName[260]; // [esp+Ch] [ebp-108h] BYREF

  Resource = GetResource("RUNPROGRAM", 0, 0);
  v1 = LocalAlloc(0x40u, Resource + 1);
  v2 = v1;
  if ( !v1 )
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  if ( !GetResource("RUNPROGRAM", v1, Resource) )
  {
    MsgBox2Param(0, 0x4B1u, 0, 0, 0x10u, 0);
    LocalFree(v2);
    g_dwExitCode = -2147023084;
    return 0;
  }
  if ( !lstrcmpA((LPCSTR)v2, "<None>") )
    dword_409A30 = 1;
  LocalFree(v2);
  if ( szStart )
  {
    if ( szStart != 92 || (v4 = 0, byte_408B3F != 92) )
      v4 = 1;
    if ( !CreateAndValidateSubdir(&szStart, 0, v4) )
    {
      MsgBox2Param(0, 0x4BEu, 0, 0, 0x10u, 0);
      return 0;
    }
    return 1;
  }
  if ( !dword_408A24 && !dword_409A30 )
  {
    if ( GetTempPathA(0x104u, &PathName)
      && (CreateAndValidateSubdir(&PathName, 1, 3)
       || !IsWindowsDrive(&PathName) && CreateAndValidateSubdir(&PathName, 1, 1)) )
    {
      return 1;
    }
    while ( 1 )
    {
      StringCopyWorkerA(v5, (size_t)"A:\\", (size_t *)v5, v13, v14);
      if ( RootPathName[0] <= 90 )
        break;
LABEL_43:
      GetWindowsDirectoryA(RootPathName, 0x104u);
      if ( !IsEnoughSpace(RootPathName, 4) )
        return 0;
    }
    while ( 1 )
    {
      DriveTypeA = GetDriveTypeA(RootPathName);
      v7 = DriveTypeA;
      if ( (DriveTypeA == 6 || DriveTypeA == 3) && GetFileAttributesA(RootPathName) != -1 )
        goto LABEL_49;
      if ( v7 == 2 )
      {
        v8 = RootPathName[0];
        if ( RootPathName[0] == 65 || RootPathName[0] == 66 )
          goto LABEL_29;
        if ( (unsigned int)GetSpace(RootPathName) >= 0x19000 )
        {
LABEL_49:
          if ( IsEnoughSpace(RootPathName, 0) || !IsWindowsDrive(RootPathName) && IsEnoughSpace(RootPathName, 0) )
          {
            if ( IsWindowsDrive(RootPathName) )
              GetWindowsDirectoryA(RootPathName, 0x104u);
            AddPath(RootPathName, (STRSAFE_LPSTR)"msdownld.tmp");
            FileAttributesA = GetFileAttributesA(RootPathName);
            if ( FileAttributesA == -1 )
              DirectoryA = CreateDirectoryA(RootPathName, 0);
            else
              DirectoryA = FileAttributesA & 0x10;
            if ( DirectoryA )
            {
              SetFileAttributesA(RootPathName, 2u);
              StringCopyWorkerA(v12, (size_t)RootPathName, (size_t *)v12, v13, v14);
              if ( CreateAndValidateSubdir(&PathName, 1, 0) )
                return 1;
              v9 = RootPathName[0];
            }
            else
            {
              v9 = RootPathName[0] + 1;
              RootPathName[3] = 0;
              ++RootPathName[0];
            }
            goto LABEL_42;
          }
        }
      }
      v8 = RootPathName[0];
LABEL_29:
      v9 = v8 + 1;
      RootPathName[0] = v9;
LABEL_42:
      if ( v9 > 90 )
        goto LABEL_43;
    }
  }
  return MyDialogBox(0, TempDirDlgProc, 0, 0) != 0;
}


int __thiscall IsGoodTempDir(char *lpFileName)
{
  CHAR *v2; // ebx
  DWORD FileAttributesA; // eax
  size_t v5; // [esp+0h] [ebp-10h]
  const char *v6; // [esp+4h] [ebp-Ch]
  HANDLE hObject; // [esp+Ch] [ebp-4h]

  v2 = (CHAR *)LocalAlloc(0x40u, strlen(lpFileName) + 20);
  if ( !v2 )
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
LABEL_3:
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  StringCchCopyA(lpFileName, v5, v6);
  AddPath(v2, (STRSAFE_LPSTR)"TMP4351$.TMP");
  hObject = CreateFileA(v2, 0x40000000u, 0, 0, 1u, 0x4000080u, 0);
  LocalFree(v2);
  if ( hObject == (HANDLE)-1 )
    goto LABEL_3;
  CloseHandle(hObject);
  FileAttributesA = GetFileAttributesA(lpFileName);
  if ( FileAttributesA == -1 || (FileAttributesA & 0x10) == 0 )
    goto LABEL_3;
  g_dwExitCode = 0;
  return 1;
}


BOOL __fastcall IsEnoughSpace(LPCSTR lpPathName, int a2, int a3)
{
  unsigned int v5; // edi
  DWORD v6; // eax
  UINT v7; // edx
  _BYTE *v8; // ecx
  int v9; // edx
  int v10; // esi
  char v11; // al
  int v12; // edx
  unsigned __int16 i; // ax
  unsigned int v14; // edx
  unsigned int v15; // ecx
  bool v16; // cc
  DWORD LastError; // eax
  DWORD MaximumComponentLength; // [esp+8h] [ebp-330h] BYREF
  DWORD FileSystemFlags; // [esp+Ch] [ebp-32Ch] BYREF
  DWORD v20; // [esp+10h] [ebp-328h]
  DWORD TotalNumberOfClusters; // [esp+14h] [ebp-324h] BYREF
  int v22; // [esp+18h] [ebp-320h]
  DWORD NumberOfFreeClusters; // [esp+1Ch] [ebp-31Ch] BYREF
  DWORD SectorsPerCluster; // [esp+20h] [ebp-318h] BYREF
  DWORD BytesPerSector; // [esp+24h] [ebp-314h] BYREF
  CHAR v26[512]; // [esp+28h] [ebp-310h] BYREF
  CHAR Buffer[260]; // [esp+228h] [ebp-110h] BYREF
  _BYTE v28[8]; // [esp+32Ch] [ebp-Ch] BYREF

  v22 = a2;
  GetCurrentDirectoryA(0x104u, Buffer);
  if ( !SetCurrentDirectoryA(lpPathName) )
  {
    MsgBox2Param(0, 0x4BCu, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  SectorsPerCluster = 0;
  BytesPerSector = 0;
  NumberOfFreeClusters = 0;
  TotalNumberOfClusters = 0;
  if ( !GetDiskFreeSpaceA(0, &SectorsPerCluster, &BytesPerSector, &NumberOfFreeClusters, &TotalNumberOfClusters)
    || (v20 = SectorsPerCluster * BytesPerSector,
        (v5 = MulDiv(SectorsPerCluster * BytesPerSector, NumberOfFreeClusters, 1024)) == 0) )
  {
    memset(v26, 0, sizeof(v26));
    g_dwExitCode = MyGetLastError();
    LastError = GetLastError();
    FormatMessageA(0x1000u, 0, LastError, 0, v26, 0x200u, 0);
    v7 = 1200;
    goto LABEL_31;
  }
  if ( !GetVolumeInformationA(0, 0, 0, 0, &MaximumComponentLength, &FileSystemFlags, 0, 0) )
  {
    memset(v26, 0, sizeof(v26));
    g_dwExitCode = MyGetLastError();
    v6 = GetLastError();
    FormatMessageA(0x1000u, 0, v6, 0, v26, 0x200u, 0);
    v7 = 1273;
LABEL_31:
    MsgBox2Param(0, v7, lpPathName, v26, 0x10u, 0);
    SetCurrentDirectoryA(Buffer);
    return 0;
  }
  SetCurrentDirectoryA(Buffer);
  v8 = v28;
  v9 = 6;
  v10 = lpPathName - v28;
  do
  {
    if ( v9 == 4 )
      break;
    v11 = v8[v10];
    if ( !v11 )
      break;
    *v8++ = v11;
    --v9;
  }
  while ( v9 );
  if ( !v9 )
    --v8;
  *v8 = 0;
  v12 = 512;
  for ( i = 0; i < 8u; ++i )
  {
    if ( v20 == v12 )
      break;
    v12 *= 2;
  }
  if ( i == 8 )
  {
    MsgBox2Param(0, 0x4C5u, 0, 0, 0x10u, 0);
    return 0;
  }
  if ( (dword_409A34 & 8) != 0 && (FileSystemFlags & 0x8000) != 0 )
  {
    v14 = 2 * g_dwFileSizes[i];
    v15 = dword_409A38 + ((unsigned int)dword_409A38 >> 2);
  }
  else
  {
    v15 = dword_409A38;
    v14 = g_dwFileSizes[i];
  }
  if ( (v22 & 3) == 3 )
  {
    v16 = v15 + v14 <= v5;
  }
  else if ( (v22 & 1) != 0 )
  {
    v16 = v14 <= v5;
  }
  else
  {
    v16 = v15 <= v5;
  }
  if ( !v16 )
    return DiskSpaceErrMsg(a3, v14, v15, (int)v28);
  g_dwExitCode = 0;
  return 1;
}


int __fastcall RemoveLeadTailBlanks(char *a1, _DWORD *a2)
{
  int v3; // esi
  char i; // al
  char *v5; // edx
  unsigned int v7; // ecx
  char v8; // al

  v3 = 0;
  for ( i = *a1; i && (i == 32 || i == 9 || i == 13 || i == 10 || i == 11 || i == 12); i = a1[v3] )
    ++v3;
  v5 = &a1[v3];
  if ( !a1[v3] )
    return 0;
  v7 = strlen(&a1[v3]);
  while ( (--v7 & 0x80000000) == 0 )
  {
    v8 = v5[v7];
    if ( v8 != 32 && v8 != 9 && v8 != 13 && v8 != 10 && v8 != 11 && v8 != 12 )
      break;
  }
  a1[v7 + 1 + v3] = 0;
  *a2 = v3;
  return 1;
}


int __thiscall ParseCmdLine(LPSTR lpsz)
{
  int v1; // edi
  CHAR v2; // al
  LPSTR v3; // eax
  unsigned int v4; // ecx
  int v5; // esi
  int v6; // ebx
  unsigned int v7; // edx
  CHAR v8; // al
  CHAR v9; // al
  int v10; // eax
  int v11; // eax
  int v12; // eax
  int v13; // eax
  int v14; // eax
  int v15; // eax
  int v16; // eax
  char v17; // cl
  char *v18; // esi
  int v19; // eax
  int v20; // eax
  int v21; // eax
  int v22; // eax
  int v23; // eax
  __int16 v24; // ax
  unsigned __int8 v25; // al
  char v26; // cl
  char *v27; // esi
  int v28; // eax
  int v29; // eax
  int v30; // ebx
  const CHAR *v31; // esi
  int v33; // ebx
  size_t v34; // [esp+0h] [ebp-11Ch]
  const char *v35; // [esp+4h] [ebp-118h]
  int v36; // [esp+Ch] [ebp-110h] BYREF
  LPSTR v37; // [esp+10h] [ebp-10Ch]
  char v38; // [esp+14h] [ebp-108h] BYREF
  CHAR String2; // [esp+15h] [ebp-107h] BYREF
  char v40; // [esp+16h] [ebp-106h]
  char v41[257]; // [esp+17h] [ebp-105h] BYREF

  v1 = 1;
  if ( !lpsz || !*lpsz )
    return 1;
  while ( 1 )
  {
    if ( !v1 )
      goto LABEL_36;
    while ( 1 )
    {
      v2 = *lpsz;
      if ( *lpsz != 32 && v2 != 9 && v2 != 13 && v2 != 10 && v2 != 11 && v2 != 12 )
        break;
      lpsz = CharNextA(lpsz);
    }
    v37 = lpsz;
    if ( !v2 )
      goto LABEL_36;
    v3 = v37;
    v4 = 0;
    v5 = 0;
    v6 = 0;
    v7 = 1;
    do
    {
      if ( v5 )
      {
        if ( v6 )
          break;
      }
      else
      {
        v8 = *v3;
        if ( v8 == 32 || v8 == 9 || v8 == 13 || v8 == 10 || v8 == 11 || v8 == 12 )
          break;
        v3 = v37;
      }
      v9 = *v3;
      if ( v9 == 34 )
      {
        if ( v37[1] == 34 )
        {
          if ( v7 >= 0x104 )
            return 0;
          *(&v38 + v4++) = 34;
          ++v7;
          v10 = 2;
        }
        else
        {
          v10 = 1;
          if ( v5 )
            v6 = 1;
          else
            v5 = 1;
        }
      }
      else
      {
        if ( v7 >= 0x104 )
          return 0;
        *(&v38 + v4++) = v9;
        ++v7;
        v10 = 1;
      }
      v37 += v10;
      v3 = v37;
    }
    while ( *v37 );
    if ( v4 >= 0x104 )
      __report_rangecheckfailure();
    *(&v38 + v4) = 0;
    if ( !v5 )
      break;
    if ( !v6 )
      goto LABEL_35;
LABEL_41:
    if ( v38 != 47 && v38 != 45 )
      return 0;
    v11 = (char)CharUpperA((LPSTR)String2) - 63;
    if ( !v11 )
    {
      MsgBox2Param(0, 0x521u, pszCabPath, 0, 0x40u, 0);
      if ( g_hMutex )
        CloseHandle(g_hMutex);
      ExitProcess(0);
    }
    v12 = v11 - 4;
    if ( !v12 )
    {
      if ( !v40 )
      {
        dword_408A24 = 1;
        goto LABEL_51;
      }
      if ( v40 == 58 )
      {
        v33 = (v41[0] == 34) + 3;
        if ( strlen(&v38 + v33) )
        {
          if ( (!ANSIStrChr(&v38 + v33) || ANSIStrChr(&v38 + v33))
            && (!ANSIStrChr(&v38 + v33) || ANSIStrChr(&v38 + v33)) )
          {
            v36 = v33;
            if ( RemoveLeadTailBlanks(&v38 + v33, &v36) )
            {
              StringCchCopyA(&v38 + v33 + v36, v34, v35);
              goto LABEL_51;
            }
          }
        }
      }
LABEL_50:
      v1 = 0;
      goto LABEL_51;
    }
    v13 = v12 - 1;
    if ( v13 )
    {
      v14 = v13 - 10;
      if ( !v14 )
      {
        if ( !v40 )
        {
          dword_408A2C = 1;
          goto LABEL_51;
        }
        if ( v40 == 58 )
        {
          v26 = v41[0];
          if ( v41[0] )
          {
            v27 = v41;
            do
            {
              ++v27;
              v28 = (char)CharUpperA((LPSTR)v26) - 69;
              if ( v28 )
              {
                v29 = v28 - 2;
                if ( v29 )
                {
                  if ( v29 == 15 )
                    dword_408A34 = 1;
                  else
                    v1 = 0;
                }
                else
                {
                  dword_408A30 = 1;
                }
              }
              else
              {
                dword_408A2C = 1;
              }
              v26 = *v27;
            }
            while ( *v27 );
          }
          goto LABEL_51;
        }
        goto LABEL_50;
      }
      v15 = v14 - 3;
      if ( !v15 )
      {
        if ( !v40 )
          goto LABEL_77;
        if ( v40 == 58 )
        {
          v25 = (unsigned __int8)CharUpperA((LPSTR)v41[0]);
          switch ( v25 )
          {
            case '1':
              goto LABEL_77;
            case 'A':
              v24 = 1;
              goto LABEL_84;
            case 'U':
LABEL_77:
              v24 = 2;
LABEL_84:
              word_408A38 = v24;
              goto LABEL_51;
          }
        }
        goto LABEL_50;
      }
      v16 = v15 - 1;
      if ( !v16 )
      {
        if ( !v40 )
        {
          dword_409A2C = 3;
          dword_408A28 = 1;
          goto LABEL_51;
        }
        if ( v40 == 58 )
        {
          v17 = v41[0];
          dword_409A2C = 1;
          if ( !v41[0] )
            goto LABEL_51;
          v18 = v41;
          while ( 2 )
          {
            ++v18;
            v19 = (char)CharUpperA((LPSTR)v17) - 65;
            if ( v19 )
            {
              v20 = v19 - 3;
              if ( v20 )
              {
                v21 = v20 - 5;
                if ( !v21 )
                {
                  dword_409A2C &= ~2u;
                  goto LABEL_71;
                }
                v22 = v21 - 5;
                if ( !v22 )
                {
                  dword_409A2C &= ~1u;
                  goto LABEL_71;
                }
                v23 = v22 - 2;
                if ( v23 )
                {
                  if ( v23 != 3 )
                  {
                    v1 = 0;
                    goto LABEL_72;
                  }
                  dword_409A2C |= 4u;
LABEL_71:
                  dword_408A28 = 1;
                }
                else
                {
                  dword_408D48 |= 0x80u;
                }
              }
              else
              {
                dword_408D48 |= 0x40u;
              }
LABEL_72:
              v17 = *v18;
              if ( !*v18 )
                goto LABEL_51;
              continue;
            }
            break;
          }
          dword_409A2C |= 2u;
          goto LABEL_71;
        }
        if ( CompareStringA(0x7Fu, 1u, "RegServer", -1, &String2, -1) == 2 )
          goto LABEL_51;
        goto LABEL_50;
      }
      if ( v16 != 2 )
        goto LABEL_50;
    }
    if ( v40 != 58 )
      goto LABEL_50;
    v30 = (v41[0] == 34) + 3;
    if ( !strlen(&v38 + v30) )
      goto LABEL_50;
    v36 = (v41[0] == 34) + 3;
    if ( !RemoveLeadTailBlanks(&v38 + v30, &v36) )
      goto LABEL_50;
    v31 = &szStart;
    if ( (unsigned __int8)CharUpperA((LPSTR)String2) != 84 )
      v31 = &byte_408A3A;
    StringCchCopyA(&v38 + v30 + v36, v34, v35);
    AddPath(v31, (STRSAFE_LPSTR)pszCabPath);
    if ( !IsFullPath((int)v31) )
      return 0;
LABEL_51:
    lpsz = v37;
    if ( !*v37 )
      goto LABEL_36;
  }
  if ( !v6 )
    goto LABEL_41;
LABEL_35:
  v1 = 0;
LABEL_36:
  if ( dword_408A2C && !szStart )
  {
    if ( GetModuleFileNameA(g_hInst, &szStart, 0x104u) )
      *(_BYTE *)(ANSIStrRChr(&szStart) + 1) = 0;
    else
      return 0;
  }
  return v1;
}


BOOL __stdcall CheckWinDir()
{
  CHAR Buffer[260]; // [esp+0h] [ebp-108h] BYREF

  if ( GetWindowsDirectoryA(Buffer, 0x104u) )
    return IsEnoughSpace(Buffer, 2, 2);
  MsgBox2Param(0, 0x4F0u, 0, 0, 0x10u, 0);
  g_dwExitCode = MyGetLastError();
  return 0;
}


signed int __stdcall MyGetLastError()
{
  signed int result; // eax

  result = GetLastError();
  if ( result > 0 )
    return (unsigned __int16)result | 0x80070000;
  return result;
}


int __thiscall TravelUpdatedFiles(int (__thiscall *this)(_DWORD, _DWORD, _DWORD, const char *, const char *))
{
  int v1; // ebx
  HGLOBAL Resource; // eax
  const char *v3; // eax
  char *v4; // edi
  HRSRC ResourceA; // eax
  int v7; // [esp+Ch] [ebp-20h]
  char pszDest[20]; // [esp+14h] [ebp-18h] BYREF

  v7 = 0;
  v1 = 1;
  StringCchPrintfA(pszDest, 0x14u, "UPDFILE%lu", 0);
  while ( 1 )
  {
    ResourceA = FindResourceA(0, pszDest, (LPCSTR)0xA);
    if ( !ResourceA )
      break;
    Resource = LoadResource(0, ResourceA);
    v3 = (const char *)LockResource(Resource);
    v4 = (char *)v3;
    if ( !v3 )
    {
      g_dwExitCode = -2147023084;
      return 0;
    }
    if ( !this(this, *(_DWORD *)v3, *((_DWORD *)v3 + 1), v3 + 8, &v3[strlen(v3 + 8) + 9]) )
    {
      v1 = 0;
      FreeResource(v4);
      return v1;
    }
    FreeResource(v4);
    StringCchPrintfA(pszDest, 0x14u, "UPDFILE%lu", ++v7);
  }
  return v1;
}


int __stdcall ProcessUpdatedFile_Size(unsigned int a1, int a2, int a3, int a4)
{
  unsigned int v4; // esi
  unsigned int i; // ecx
  int v6; // edx
  unsigned int v7; // eax

  v4 = 512;
  for ( i = 0; i < 8; ++i )
  {
    v6 = a1 % v4;
    v7 = a1 % v4 != 0 ? v4 : 0;
    v4 *= 2;
    g_dwFileSizes[i] += a1 + v7 - v6;
  }
  return 1;
}


int __thiscall ProcessUpdatedFile_Write(
        size_t *pcchNewDestLength,
        DWORD nNumberOfBytesToWrite,
        int a3,
        STRSAFE_LPSTR pszDest,
        const void *a5)
{
  int v5; // edi
  HANDLE FileA; // esi
  const char *v8; // [esp+0h] [ebp-11Ch]
  size_t v9; // [esp+4h] [ebp-118h]
  DWORD NumberOfBytesWritten; // [esp+10h] [ebp-10Ch] BYREF
  CHAR FileName[260]; // [esp+14h] [ebp-108h] BYREF

  NumberOfBytesWritten = 0;
  v5 = 1;
  StringCopyWorkerA((STRSAFE_LPSTR)pcchNewDestLength, (size_t)&PathName, pcchNewDestLength, v8, v9);
  AddPath(FileName, pszDest);
  FileA = CreateFileA(FileName, 0x40000000u, 0, 0, 2u, 0x80u, 0);
  if ( FileA == (HANDLE)-1 )
  {
    g_dwExitCode = -2147024814;
    return 0;
  }
  else
  {
    if ( !WriteFile(FileA, a5, nNumberOfBytesToWrite, &NumberOfBytesWritten, 0)
      || nNumberOfBytesToWrite != NumberOfBytesWritten )
    {
      g_dwExitCode = -2147024814;
      v5 = 0;
    }
    CloseHandle(FileA);
  }
  return v5;
}


HMODULE __thiscall MyLoadLibrary(size_t *pcchNewDestLength)
{
  DWORD FileAttributesA; // eax
  const char *v3; // [esp+0h] [ebp-10Ch]
  size_t FileName[65]; // [esp+4h] [ebp-108h] BYREF

  StringCopyWorkerA((STRSAFE_LPSTR)pcchNewDestLength, (size_t)&PathName, pcchNewDestLength, v3, FileName[0]);
  AddPath((LPCSTR)FileName, (STRSAFE_LPSTR)"advpack.dll");
  FileAttributesA = GetFileAttributesA((LPCSTR)FileName);
  if ( FileAttributesA == -1 || (FileAttributesA & 0x10) != 0 )
    return LoadLibraryA("advpack.dll");
  else
    return LoadLibraryExA((LPCSTR)FileName, 0, 8u);
}


INT_PTR __fastcall MyDialogBox(
        int a1,
        const CHAR *a2,
        HWND hWndParent,
        INT_PTR (__stdcall *lpDialogFunc)(HWND, UINT, WPARAM, LPARAM),
        LPARAM dwInitParam,
        int a6)
{
  HINSTANCE v6; // esi
  HRSRC ResourceA; // eax
  const DLGTEMPLATE *Resource; // eax
  DLGTEMPLATE *v9; // edi
  INT_PTR v10; // eax
  INT_PTR v11; // esi

  v6 = g_hInst;
  ResourceA = FindResourceA(g_hInst, a2, (LPCSTR)5);
  if ( !ResourceA
    || (Resource = (const DLGTEMPLATE *)LoadResource(v6, ResourceA), (v9 = (DLGTEMPLATE *)Resource) == 0)
    || (dwInitParam
      ? (v10 = DialogBoxIndirectParamA(v6, Resource, hWndParent, lpDialogFunc, dwInitParam))
      : (v10 = DialogBoxIndirectParamA(v6, Resource, hWndParent, lpDialogFunc, 0)),
        v11 = v10,
        FreeResource(v9),
        v11 == -1) )
  {
    MsgBox2Param(0, 0x4FBu, 0, 0, 0x10u, 0);
    return a6;
  }
  return v11;
}


HRESULT __fastcall AddPath(CHAR *lpszStart, unsigned int a2, STRSAFE_LPSTR pszDest)
{
  unsigned int v4; // esi
  CHAR *v6; // esi
  size_t v8; // [esp+0h] [ebp-Ch]
  const char *v9; // [esp+4h] [ebp-8h]

  v4 = strlen(lpszStart);
  if ( v4 + 1 >= a2 )
    return -2147024774;
  v6 = &lpszStart[v4];
  if ( v6 > lpszStart && *CharPrevA(lpszStart, v6) != 92 )
    *v6++ = 92;
  *v6 = 0;
  while ( *pszDest == 32 )
    ++pszDest;
  return StringCchCatA(pszDest, v8, v9);
}


int __thiscall GetParentDir(LPCSTR lpszStart)
{
  int v2; // ebx
  const CHAR *i; // eax
  const CHAR *v4; // esi
  const CHAR *v6; // [esp-4h] [ebp-10h]

  v2 = 0;
  v6 = CharPrevA(lpszStart, &lpszStart[strlen(lpszStart)]);
  for ( i = CharPrevA(lpszStart, v6); ; i = CharPrevA(lpszStart, i) )
  {
    v4 = i;
    if ( i <= lpszStart )
      break;
    if ( *i == 92 )
      goto LABEL_6;
  }
  if ( *i != 92 )
    return v2;
LABEL_6:
  if ( i == lpszStart || *CharPrevA(lpszStart, i) == 58 )
    v4 = CharNextA(v4);
  *v4 = 0;
  return 1;
}


BOOL __fastcall ChrCmpA_inline(__int16 TestChar, __int16 a2)
{
  if ( (_BYTE)TestChar != (_BYTE)a2 )
    return 1;
  if ( IsDBCSLeadByte(TestChar) )
    return TestChar != a2;
  return 0;
}


LPSTR __fastcall ANSIStrChr(LPSTR lpsz, __int16 a2)
{
  while ( 1 )
  {
    if ( !*lpsz )
      return 0;
    if ( !ChrCmpA_inline(*(_WORD *)lpsz, a2) )
      break;
    lpsz = CharNextA(lpsz);
  }
  return lpsz;
}


BOOL __thiscall FileExists(LPCSTR lpFileName)
{
  DWORD FileAttributesA; // eax

  FileAttributesA = GetFileAttributesA(lpFileName);
  return FileAttributesA != -1 && (FileAttributesA & 0x10) == 0;
}


LPSTR __fastcall ANSIStrRChr(LPSTR lpsz, __int16 a2)
{
  LPSTR v4; // edi

  v4 = 0;
  while ( *lpsz )
  {
    if ( !ChrCmpA_inline(*(_WORD *)lpsz, a2) )
      v4 = lpsz;
    lpsz = CharNextA(lpsz);
  }
  return v4;
}


BOOL __fastcall ConvertHexStringToIntA(LPCSTR lpsz, int *a2)
{
  int v2; // esi
  const CHAR *i; // edi
  char v4; // bl

  v2 = 0;
  for ( i = lpsz; ; i = CharNextA(i) )
  {
    v4 = *i;
    if ( (unsigned __int8)(*i - 48) <= 9u )
    {
      v2 = v4 + 16 * (v2 - 3);
      continue;
    }
    if ( v4 >= 97 )
      v4 -= 32;
    if ( (unsigned int)(v4 - 65) > 5 )
      break;
    v2 = v4 + 16 * v2 - 55;
  }
  *a2 = v2;
  return i != lpsz;
}


BOOL __stdcall EnumResLangProc(HMODULE hModule, LPCSTR lpType, LPCSTR lpName, WORD wLanguage, LONG_PTR lParam)
{
  int v5; // esi

  v5 = 1;
  if ( lpType == *(LPCSTR *)(lParam + 8) && *(_WORD *)lParam == (wLanguage & 0x3FF) )
  {
    *(_DWORD *)(lParam + 4) = 1;
    v5 = 0;
    *(_WORD *)lParam = wLanguage;
  }
  return v5;
}


int __thiscall GetResourceLanguage(HMODULE hModule, int a2, __int16 a3)
{
  LONG_PTR lParam; // [esp+0h] [ebp-Ch] BYREF
  int v5; // [esp+4h] [ebp-8h]
  int v6; // [esp+8h] [ebp-4h]

  v5 = 0;
  LOWORD(lParam) = a3;
  v6 = 16;
  EnumResourceLanguagesA(hModule, (LPCSTR)0x10, (LPCSTR)1, EnumResLangProc, (LONG_PTR)&lParam);
  return v5;
}


int __thiscall IsBiDiLocalizedBinary(void *this, int a2)
{
  int v2; // esi
  HMODULE v3; // edi
  int v4; // ecx

  v2 = dword_4081D4;
  v3 = g_hInst;
  if ( dword_4081D4 == -2 )
  {
    dword_4081D4 = 0;
    v2 = 1;
    if ( GetResourceLanguage(g_hInst, (int)this, 1) || GetResourceLanguage(v3, v4, 13) )
      dword_4081D4 = 1;
    else
      return dword_4081D4;
  }
  return v2;
}


int __stdcall RunningOnWin95BiDiLoc()
{
  int v0; // edi
  LSTATUS v1; // esi
  int v2; // eax
  DWORD Type; // [esp+8h] [ebp-B4h] BYREF
  DWORD cbData; // [esp+Ch] [ebp-B0h] BYREF
  int v6; // [esp+10h] [ebp-ACh] BYREF
  HKEY phkResult; // [esp+14h] [ebp-A8h] BYREF
  struct _OSVERSIONINFOA VersionInformation; // [esp+18h] [ebp-A4h] BYREF
  BYTE Data[12]; // [esp+ACh] [ebp-10h] BYREF

  v0 = dword_4081D8;
  cbData = 12;
  v6 = 0;
  if ( dword_4081D8 == -2 )
  {
    dword_4081D8 = 0;
    VersionInformation.dwOSVersionInfoSize = 148;
    if ( GetVersionExA(&VersionInformation)
      && (v0 = 1, VersionInformation.dwPlatformId == 1)
      && VersionInformation.dwMajorVersion == 4
      && VersionInformation.dwMinorVersion < 0xA
      && GetSystemMetrics(74)
      && !RegOpenKeyExA(HKEY_CURRENT_USER, "Control Panel\\Desktop\\ResourceLocale", 0, 0x20019u, &phkResult)
      && (v1 = RegQueryValueExA(phkResult, pszCabPath, 0, &Type, Data, &cbData), RegCloseKey(phkResult), !v1)
      && ConvertHexStringToIntA((LPCSTR)Data, &v6)
      && ((v2 = v6 & 0x3FF, v2 == 1) || v2 == 13) )
    {
      dword_4081D8 = 1;
    }
    else
    {
      return dword_4081D8;
    }
  }
  return v0;
}


int __thiscall GetSpace(LPCSTR lpRootPathName)
{
  int v1; // esi
  bool v2; // zf
  DWORD NumberOfFreeClusters; // [esp+4h] [ebp-10h] BYREF
  DWORD TotalNumberOfClusters; // [esp+8h] [ebp-Ch] BYREF
  DWORD SectorsPerCluster; // [esp+Ch] [ebp-8h] BYREF
  DWORD BytesPerSector; // [esp+10h] [ebp-4h] BYREF

  v1 = 0;
  v2 = *lpRootPathName == 0;
  SectorsPerCluster = 0;
  BytesPerSector = 0;
  NumberOfFreeClusters = 0;
  TotalNumberOfClusters = 0;
  if ( !v2
    && GetDiskFreeSpaceA(
         lpRootPathName,
         &SectorsPerCluster,
         &BytesPerSector,
         &NumberOfFreeClusters,
         &TotalNumberOfClusters) )
  {
    return MulDiv(SectorsPerCluster * BytesPerSector, TotalNumberOfClusters, 1024);
  }
  return v1;
}


int pre_cpp_init()
{
  int result; // eax

  dword_4081FC = _newmode;
  result = ___getmainargs(&unk_4081E8, &unk_4081EC, &unk_4081F0, _dowildcard, &dword_4081FC);
  dword_4081F4 = result;
  return result;
}


int WinMainCRTStartup()
{
  __security_init_cookie();
  return _mainCRTStartup();
}


int _mainCRTStartup()
{
  PVOID StackBase; // esi
  int v1; // edi
  signed __int32 v2; // eax
  int result; // eax
  char *v4; // esi
  BOOL v5; // edi
  unsigned __int8 v6; // cl
  int wShowWindow; // eax
  _STARTUPINFOW StartupInfo; // [esp+10h] [ebp-68h] BYREF
  BOOL v9; // [esp+58h] [ebp-20h]
  char *v10; // [esp+5Ch] [ebp-1Ch]
  CPPEH_RECORD ms_exc; // [esp+60h] [ebp-18h]

  v9 = 0;
  GetStartupInfoW(&StartupInfo);
  ms_exc.registration.TryLevel = 0;
  StackBase = NtCurrentTeb()->NtTib.StackBase;
  v1 = 0;
  while ( 1 )
  {
    v2 = _InterlockedCompareExchange(&__native_startup_lock, (signed __int32)StackBase, 0);
    if ( !v2 )
      break;
    if ( (PVOID)v2 == StackBase )
    {
      v1 = 1;
      break;
    }
    Sleep(0x3E8u);
  }
  if ( __native_startup_state == 1 )
  {
    _amsg_exit(31);
  }
  else if ( __native_startup_state )
  {
    dword_4081E4 = 1;
  }
  else
  {
    __native_startup_state = 1;
    if ( _initterm_e((_PIFV *)&__xi_a, (_PIFV *)&__xi_z) )
    {
      ms_exc.registration.TryLevel = -2;
      return 255;
    }
  }
  if ( __native_startup_state == 1 )
  {
    _initterm((_PVFV *)&__xc_a, (_PVFV *)&__xc_z);
    __native_startup_state = 2;
  }
  if ( !v1 )
    _InterlockedExchange(&__native_startup_lock, 0);
  if ( __dyn_tls_init_callback && _IsNonwritableInCurrentImage(&__dyn_tls_init_callback) )
    __dyn_tls_init_callback(__dyn_tls_init_callback, 0, 2, 0);
  v4 = __acmdln;
  v10 = __acmdln;
  v5 = v9;
  while ( 1 )
  {
    v6 = *v4;
    if ( (unsigned __int8)*v4 <= 0x20u )
    {
      if ( !v6 )
        goto LABEL_26;
      if ( !v5 )
        break;
    }
    if ( v6 == 34 )
    {
      v5 = !v5;
      v9 = v5;
    }
    if ( __ismbblead(v6) )
      v10 = ++v4;
    v10 = ++v4;
  }
  while ( v6 && v6 <= 0x20u )
  {
    v10 = ++v4;
    v6 = *v4;
  }
LABEL_26:
  if ( (StartupInfo.dwFlags & 1) != 0 )
    wShowWindow = StartupInfo.wShowWindow;
  else
    wShowWindow = 10;
  result = WinMain((HINSTANCE)0x400000, 0, v4, wShowWindow);
  dword_4081E0 = result;
  if ( !dword_4081F8 )
    _exit(result);
  if ( !dword_4081E4 )
  {
    __cexit();
    return dword_4081E0;
  }
  return result;
}


int __cdecl _initterm_e(_PIFV *First, _PIFV *Last)
{
  _PIFV *v2; // esi
  int result; // eax

  v2 = First;
  for ( result = 0; v2 < Last; ++v2 )
  {
    if ( result )
      break;
    if ( *v2 )
      result = ((int (__thiscall *)(_PIFV))*v2)(*v2);
  }
  return result;
}


bool check_managed_app()
{
  __int16 v0; // ax
  bool v1; // zf

  if ( LOWORD(MEMORY[0x400000].unused) == 23117 && *(_DWORD *)(MEMORY[0x40003C] + 0x400000) == 17744 )
  {
    v0 = *(_WORD *)(MEMORY[0x40003C] + 4194328);
    if ( v0 == 267 )
    {
      if ( *(_DWORD *)(MEMORY[0x40003C] + 4194420) > 0xEu )
      {
        v1 = *(_DWORD *)(MEMORY[0x40003C] + 4194536) == 0;
        return !v1;
      }
    }
    else if ( v0 == 523 && *(_DWORD *)(MEMORY[0x40003C] + 4194436) > 0xEu )
    {
      v1 = *(_DWORD *)(MEMORY[0x40003C] + 4194552) == 0;
      return !v1;
    }
  }
  return 0;
}


void __fastcall __security_check_cookie(uintptr_t StackCookie)
{
  if ( StackCookie != __security_cookie )
    __report_gsfailure();
}


BOOL __cdecl __raise_securityfailure(struct _EXCEPTION_POINTERS *ExceptionInfo)
{
  HANDLE CurrentProcess; // eax

  SetUnhandledExceptionFilter(0);
  UnhandledExceptionFilter(ExceptionInfo);
  CurrentProcess = GetCurrentProcess();
  return TerminateProcess(CurrentProcess, 0xC0000409);
}


void __cdecl  __report_gsfailure()
{
  int v0; // eax
  int v1; // edx
  int v2; // ecx
  int v3; // ebx
  int v4; // edi
  int v5; // esi
  unsigned int v6; // kr00_4
  int vars0; // [esp+324h] [ebp+0h]
  int retaddr; // [esp+328h] [ebp+4h]
  char v9; // [esp+32Ch] [ebp+8h] BYREF

  dword_408300 = v0;
  dword_4082FC = v2;
  dword_4082F8 = v1;
  dword_4082F4 = v3;
  dword_4082F0 = v5;
  dword_4082EC = v4;
  word_408318 = __SS__;
  word_40830C = __CS__;
  word_4082E8 = __DS__;
  word_4082E4 = __ES__;
  word_4082E0 = __FS__;
  word_4082DC = __GS__;
  v6 = __readeflags();
  dword_408310 = v6;
  dword_408304 = vars0;
  dword_408308 = retaddr;
  dword_408314 = (int)&v9;
  dword_408250 = 65537;
  dword_40820C = retaddr;
  dword_408200 = -1073740791;
  dword_408204 = 1;
  dword_408210 = 3;
  dword_408214 = 2;
  unk_408218 = __security_cookie;
  unk_40821C = __security_cookie_complement;
  __raise_securityfailure((struct _EXCEPTION_POINTERS *)&ExceptionInfo);
}


void __usercall  __report_rangecheckfailure(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        int a7)
{
  unsigned int v7; // kr00_4
  int retaddr; // [esp+4h] [ebp+4h]

  dword_408300 = a1;
  dword_4082FC = a3;
  dword_4082F8 = a2;
  dword_4082F4 = a4;
  dword_4082F0 = a6;
  dword_4082EC = a5;
  word_408318 = __SS__;
  word_40830C = __CS__;
  word_4082E8 = __DS__;
  word_4082E4 = __ES__;
  word_4082E0 = __FS__;
  word_4082DC = __GS__;
  v7 = __readeflags();
  dword_408310 = v7;
  dword_408250 = 65537;
  dword_408308 = retaddr;
  dword_408314 = (int)&a7;
  dword_40820C = retaddr;
  dword_408200 = -1073740791;
  dword_408204 = 1;
  dword_408210 = 1;
  dword_408214 = 8;
  __raise_securityfailure((struct _EXCEPTION_POINTERS *)&ExceptionInfo);
}


LONG __stdcall __CxxUnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo)
{
  PEXCEPTION_RECORD ExceptionRecord; // eax
  ULONG_PTR v2; // eax

  ExceptionRecord = ExceptionInfo->ExceptionRecord;
  if ( ExceptionInfo->ExceptionRecord->ExceptionCode == -529697949 && ExceptionRecord->NumberParameters == 3 )
  {
    v2 = ExceptionRecord->ExceptionInformation[0];
    if ( v2 == 429065504 || v2 == 429065505 || v2 == 429065506 || v2 == 26820608 )
      terminate();
  }
  return 0;
}


int __CxxSetUnhandledExceptionFilter()
{
  SetUnhandledExceptionFilter(__CxxUnhandledExceptionFilter);
  return 0;
}


// attributes: thunk
int _XcptFilter()
{
}int __stdcall RtlpImageNtHeader(int a1)
{
  int v1; // ecx
  unsigned int v2; // edx

  v1 = 0;
  if ( a1 )
  {
    if ( a1 != -1 && *(_WORD *)a1 == 23117 )
    {
      v2 = *(_DWORD *)(a1 + 60);
      if ( v2 < 0x10000000 )
        return *(_DWORD *)(v2 + a1) == 17744 ? v2 + a1 : 0;
    }
  }
  return v1;
}


int __cdecl _get_image_app_type(int a1)
{
  HMODULE ModuleHandleW; // eax
  int v2; // eax
  int v3; // ecx
  int result; // eax

  ModuleHandleW = GetModuleHandleW(0);
  if ( !ModuleHandleW )
    return a1;
  v2 = RtlpImageNtHeader((int)ModuleHandleW);
  if ( !v2 )
    return a1;
  v3 = *(unsigned __int16 *)(v2 + 92);
  result = 2;
  if ( (_WORD)v3 == 2 )
    return result;
  if ( v3 == 3 )
    return 1;
  else
    return a1;
}


// attributes: thunk
int __cdecl _amsg_exit(int a1)
{
}int __cdecl _setargv()
{
  return 0;
}


int __cdecl _FindPESection(int a1, unsigned int a2)
{
  unsigned int v2; // edx
  int v3; // ecx
  int result; // eax
  unsigned int v5; // esi

  v2 = 0;
  v3 = a1 + *(_DWORD *)(a1 + 60);
  result = v3 + *(unsigned __int16 *)(v3 + 20) + 24;
  if ( !*(_WORD *)(v3 + 6) )
    return 0;
  while ( 1 )
  {
    v5 = *(_DWORD *)(result + 12);
    if ( a2 >= v5 && a2 < v5 + *(_DWORD *)(result + 8) )
      break;
    ++v2;
    result += 40;
    if ( v2 >= *(unsigned __int16 *)(v3 + 6) )
      return 0;
  }
  return result;
}


BOOL __cdecl _IsNonwritableInCurrentImage(int a1)
{
  int PESection; // eax

  return _ValidateImageBase(0x400000)
      && (PESection = _FindPESection(0x400000, a1 - 0x400000)) != 0
      && *(int *)(PESection + 36) >= 0;
}


BOOL __cdecl _ValidateImageBase(int a1)
{
  int v1; // eax
  BOOL result; // eax

  result = 0;
  if ( *(_WORD *)a1 == 23117 )
  {
    v1 = a1 + *(_DWORD *)(a1 + 60);
    if ( *(_DWORD *)v1 == 17744 && *(_WORD *)(v1 + 24) == 267 )
      return 1;
  }
  return result;
}


void __cdecl __security_init_cookie()
{
  uintptr_t v0; // eax
  uintptr_t v1; // ecx
  LARGE_INTEGER PerformanceCount; // [esp+8h] [ebp-14h] BYREF
  struct _FILETIME SystemTimeAsFileTime; // [esp+10h] [ebp-Ch] BYREF
  DWORD v4; // [esp+18h] [ebp-4h] BYREF

  SystemTimeAsFileTime.dwLowDateTime = 0;
  SystemTimeAsFileTime.dwHighDateTime = 0;
  v0 = __security_cookie;
  if ( __security_cookie == -1153374642 || (__security_cookie & 0xFFFF0000) == 0 )
  {
    GetSystemTimeAsFileTime(&SystemTimeAsFileTime);
    v4 = SystemTimeAsFileTime.dwLowDateTime ^ SystemTimeAsFileTime.dwHighDateTime;
    v4 ^= GetCurrentProcessId();
    v4 ^= GetCurrentThreadId();
    v4 ^= (unsigned int)&v4 ^ GetTickCount();
    QueryPerformanceCounter(&PerformanceCount);
    v0 = v4 ^ PerformanceCount.LowPart ^ PerformanceCount.HighPart;
    v1 = v0;
    if ( v0 == -1153374642 || (__security_cookie & 0xFFFF0000) == 0 )
    {
      v0 = -1153374641;
      v1 = -1153374641;
    }
    __security_cookie = v1;
  }
  __security_cookie_complement = ~v0;
}


unsigned int _setdefaultprecision()
{
  return __controlfp(0x10000u, 0x30000u);
}


// attributes: thunk
void __cdecl _initterm(_PVFV *First, _PVFV *Last)
{
}_DWORD *__cdecl _SEH_prolog4(int a1, int a2)
{
  void *v4; // esp
  void *v6; // [esp-18h] [ebp-18h]
  _DWORD v7[2]; // [esp-8h] [ebp-8h] BYREF
  _UNKNOWN *retaddr; // [esp+0h] [ebp+0h]
  int v9; // [esp+4h] [ebp+4h]

  v7[1] = _except_handler4;
  v7[0] = NtCurrentTeb()->NtTib.ExceptionList;
  v4 = alloca(a2);
  v9 = -2;
  retaddr = v6;
  return v7;
}


// positive sp value has been detected, the output may be wrong!
void _SEH_epilog4()
{
}int __cdecl _except_handler4(int a1, int a2, int a3, int a4)
{
  return _except_handler4_common(&__security_cookie, __security_check_cookie, a1, a2, a3, a4);
}


void _guard_check_icall_nop()
{
  ;
}


// attributes: thunk
int __cdecl _except_handler4_common(int a1, int a2, int a3, int a4, int a5, int a6)
{
}// attributes: thunk
void *__cdecl memcpy(void *a1, const void *Src, size_t Size)
{
}// attributes: thunk
void *__cdecl memset(void *a1, int Val, size_t Size)
{
}